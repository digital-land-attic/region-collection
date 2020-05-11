#!/usr/bin/env python3

import os
import csv
import json
import requests
import pandas as pd


def get_csv_as_json(path_to_csv):
    csv_pd = pd.read_csv(path_to_csv, sep=",")
    return json.loads(csv_pd.to_json(orient="records"))


def fetch_json_from_endpoint(endpoint):
    json_url = requests.get(endpoint)
    # should this check response is OK?
    return json_url.json()


def open_json_file(path):
    # read file
    with open(path, 'r') as f:
        data=f.read()

    return json.loads(data)


def save_geojson(data, path_to_file):
    with open(path_to_file, "w") as f:
        json.dump(data, f)


# need a method that returns dict as well as adds k:v
# useful in list comprehensions
def update_dict(d, k, val):
    d[k] = val
    return d


# write json to csv file
def json_to_csv_file(output_file, data):

    # check dirs exist first
    dirs = os.path.dirname(output_file)
    if not os.path.exists(dirs):
        os.makedirs(dirs)

    print(f"Write data to {output_file}")
    # now we will open a file for writing
    data_file = open(output_file, "w")
    # create the csv writer object
    csv_writer = csv.writer(data_file, lineterminator="\n")
    # Counter variable used for writing
    # headers to the CSV file
    count = 0
    for row in data:
        if count == 0:

            # Writing headers of CSV file
            header = row.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data of CSV file
        csv_writer.writerow(row.values())

    data_file.close()


def indexed_dict_to_csv(output_file, data, idx_name):
    data = [update_dict(v, idx_name, k) for k, v in data.items()]
    json_to_csv_file(output_file, data)
