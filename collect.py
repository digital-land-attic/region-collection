#!/usr/bin/env python3

from file_helpers import save_geojson, get_csv_as_json, fetch_json_from_endpoint, json_to_csv_file


def name_to_identifier(n):
    return n.lower().replace(" ", "-").replace(",", "")


def extract_name_from_document_url(url):
    return url.split("/")[-1]


# pass list of tuples
# (desired field name, current field name, identifier(BOOL))
def map_fields(d, field_tuples):
    entry = {}
    for (field, current, k) in field_tuples:
        entry[field] = d.get(current)
        if k:
            entry[field] = name_to_identifier(d.get(current))
    return entry


def collect_geojson(name, endpoint, filename, fields):
    print(f"Collect: {name}\nfrom: {endpoint}")
    d = fetch_json_from_endpoint(endpoint)
    # save_geojson(d, extract_name_from_document_url(region_data[2]))
    save_geojson(d, filename)
    entries = [map_fields(r["properties"], fields) for r in d["features"]]
    return entries


mappings = {
    "region": [
        ("region", "RGN19NM", True),
        ("name", "RGN19NM", False),
        ("statistical-geography", "RGN19CD", False),
    ]
}


if __name__ == "__main__":
    data_sources = get_csv_as_json("dataset/data.csv")
    # collect LRF and Region data
    for source in data_sources:
        filename = extract_name_from_document_url(source['documentation-url'])
        data = collect_geojson(source['name'], source['resource-url'], f"collection/{filename}", mappings[source['type']])
        json_to_csv_file(f"data/{source['type']}.csv", data)