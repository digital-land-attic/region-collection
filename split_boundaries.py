#!/usr/bin/env python3

import os
from file_helpers import open_json_file, save_geojson, get_csv_as_json, indexed_dict_to_csv


geojson_template = {
    'type': 'FeatureCollection',
    'features': []
}


boundary_index = {}


def get_boundary_type(t):
    return t.split("/")[1]


def extract_name_from_document_url(url):
    return url.split("/")[-1]


def make_boundary_url(stat_geo, typ):
    return f'https://raw.githubusercontent.com/digital-land/region-collection/master/collection/{typ}/{stat_geo}/index.geojson'


def split_boundaries(path, boundary_type):
    boundaries = open_json_file(path)
    for boundary in boundaries['features']:
        data = geojson_template
        data['features'] = [boundary]
        k = boundary['properties']['rgn19cd']

        boundary_index.setdefault(k, {})
        boundary_index[k][boundary_type] = make_boundary_url(k, boundary_type)

        boundary_path = f"./collection/{boundary_type}/{k}"
        os.makedirs(boundary_path, exist_ok=True)
        print(f"Saving boundary for {k} to {boundary_path}")
        save_geojson(data, f'{boundary_path}/index.geojson')


if __name__ == "__main__":
    boundary_files = get_csv_as_json("dataset/boundaries.csv")
    for typ in boundary_files:
        filename = extract_name_from_document_url(typ['documentation-url'])
        split_boundaries(f"collection/{filename}.geojson",get_boundary_type(typ['type']))
    

    indexed_dict_to_csv("index/boundaries.csv", boundary_index, 'statistical-geography')