"""
Get summary statistics for the metadata.
"""

import json
from copy import deepcopy
from typing import List
from zipfile import ZipFile

import pandas as pd
from IPython.display import display, Markdown

from _visualizations import build_visualizations


def get_path_all(path_data_source: str) -> str:
    return f"{path_data_source}/output/metadata-processed/all.zip"


def get_path_vis(path_data_source: str) -> str:
    return f"{path_data_source}/output/metadata-processed/visualizations.zip"


def load_zipped_json(path: str):
    with ZipFile(path) as zip_ref:
        for filename in zip_ref.namelist():
            with zip_ref.open(filename) as f:
                return json.load(f)


def get_markdown_data(data_sources: List) -> List:
    """
    Edit the input data sources to save information
    for generating a markdown table.
    """

    data_sources = deepcopy(data_sources)

    for d in data_sources:
        path_vis = get_path_vis(d["pathDataSource"])
        processed_metadata_vis = build_visualizations(load_zipped_json(path_vis))
        d["#oldvis"] = len(processed_metadata_vis)

        path_all = get_path_all(d["pathDataSource"])
        processed_metadata_all = load_zipped_json(path_all)
        d["#all"] = len(processed_metadata_all)

        d["name"] = f"[{d['name']}]({d['url']})"
        del d["url"]

        path_data_dir = f"{d['pathDataSource']}/output/metadata-processed/"
        d["data files"] = f"[link]({path_data_dir})"
        del d["pathDataSource"]

    data_sources.append(
        {
            "name": "Total",
            "#oldvis": sum([d["#oldvis"] for d in data_sources]),
            "#all": sum([d["#all"] for d in data_sources]),
            "data files": "/",
        }
    )

    return data_sources


def print_markdown_table(data_sources: List) -> None:
    data_sources = get_markdown_data(data_sources)
    df = pd.DataFrame(data_sources)
    display(Markdown(df.to_markdown(index=False)))


data_sources = [
    {
        "name": "Alabama Maps",
        "url": "http://alabamamaps.ua.edu/historicalmaps/",
        "pathDataSource": "../data-sources/alabama-maps",
    },
    {
        "name": "British Library Collection Items",
        "url": "https://www.bl.uk/collection-items",
        "pathDataSource": "../data-sources/british-library-collection-items",
    },
    {
        "name": "British Library Images Online",
        "url": "https://imagesonline.bl.uk/",
        "pathDataSource": "../data-sources/british-library-images-online",
    },
    {
        "name": "David Rumsey Map Collection",
        "url": "https://www.davidrumsey.com/",
        "pathDataSource": "../data-sources/david-rumsey-map-collection",
    },
    {
        "name": "Gallica",
        "url": "https://gallica.bnf.fr/",
        "pathDataSource": "../data-sources/gallica",
    },
    {
        "name": "Internet Archive",
        "url": "https://archive.org/",
        "pathDataSource": "../data-sources/internet-archive",
    },
    {
        "name": "Library of Congress",
        "url": "https://www.loc.gov/",
        "pathDataSource": "../data-sources/library-of-congress",
    },
    {
        "name": "Telefact",
        "url": "https://modley-telefact-1939-1945.tumblr.com/",
        "pathDataSource": "../data-sources/telefact",
    },
]
