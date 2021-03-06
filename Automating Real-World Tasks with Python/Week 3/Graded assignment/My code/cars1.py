#!/usr/bin/env python3

import json
import locale
import sys
import reports
import os
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename, encoding='utf-8') as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):

  """Analyzes the data, looking for maximums.Returns a list of lines that summarize the information."""

  #locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  total_sales = {"sales": 0}
  result_dict = {}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    # TODO: also handle max sales
    item_sales = item["total_sales"]
    if item_sales > total_sales["sales"]:
      item["sales"] = item_sales
      total_sales = item

    # TODO: also handle most popular car_year
    if item['car']['car_year'] not in result_dict:
      result_dict[item['car']['car_year']] = item['total_sales']
    result_dict[item['car']['car_year']] += item['total_sales']
  result_dict = sorted(result_dict.items(), reverse = True, key = lambda kv: kv[1])

  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: {}".format(format_car(total_sales["car"]), total_sales["sales"]),
    "The most popular year was {} with {} sales.".format(result_dict[0][0], result_dict[0][1])
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  summary1 = "<br/>".join(summary)
  e_body = "\n".join(summary)

  # TODO: turn this into a PDF report
  reports.generate("cars.pdf" , "Sales Summary of Last month.", summary1, table_data = cars_dict_to_table(data))
  """
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com" . format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = e_body
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)
  """
if __name__ == "__main__":
  main(sys.argv)
