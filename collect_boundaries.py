#!/usr/bin/env python3

import os
import json
import requests
import pandas as pd

from file_helpers import get_csv_as_json, fetch_json_from_endpoint, save_geojson


def extract_name_from_document_url(url):
    return url.split("/")[-1]


def collect_geojson(name, endpoint, filename):
    print(f"Collect: {name}\nfrom: {endpoint}")
    d = fetch_json_from_endpoint(endpoint)
    print(f"Save to: {filename}")
    save_geojson(d, filename)


if __name__ == "__main__":
    boundary_files = get_csv_as_json("dataset/boundaries.csv")
    for f in boundary_files:
        filename = extract_name_from_document_url(f['documentation-url'])
        collect_geojson(f['name'], f['resource-url'], f"./collection/{filename}.geojson")
