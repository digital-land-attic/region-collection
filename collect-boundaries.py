#!/usr/bin/env python3

import os
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


def save_geojson(data, filename):
    with open(f"collection/{filename}.geojson", "w") as f:
        json.dump(data, f)


def extract_name_from_document_url(url):
    return url.split("/")[-1]


def collect_geojson(name, endpoint, filename):
    print(f"Collect: {name}\nfrom: {endpoint}")
    d = fetch_json_from_endpoint(endpoint)
    # save_geojson(d, extract_name_from_document_url(region_data[2]))
    save_geojson(d, filename)


if __name__ == "__main__":
    boundary_files = get_csv_as_json("dataset/boundaries.csv")
    for f in boundary_files:
        filename = extract_name_from_document_url(f['documentation-url'])
        collect_geojson(f['name'], f['resource-url'], filename)
