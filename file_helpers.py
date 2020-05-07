#!/usr/bin/env python3

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

