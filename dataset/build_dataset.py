"""
The script to construct a collection of "visualization" and "author" entities from the metadata.
The metadata of multiple data sources are combined.

Side effects of this script:
- The visualizations will be stored in "visualizations.json".
- The authors will be stored in "authors.json".
"""

import json
import os

from builders import build_authors, build_visualizations
from _loader import load_processed_metadata


if __name__ == "__main__":
    output_dir = "./output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    path_data_sources = "../data-sources"
    dataset_names = [
        f"{path_data_sources}/alabama-maps",
        f"{path_data_sources}/british-library-collection-items",
        f"{path_data_sources}/british-library-images-online",
        f"{path_data_sources}/david-rumsey-map-collection",
        f"{path_data_sources}/gallica",
        f"{path_data_sources}/internet-archive",
        f"{path_data_sources}/library-of-congress",
        f"{path_data_sources}/telefact",
    ]
    processed_metadata = load_processed_metadata(dataset_paths=dataset_names)

    visualizations = build_visualizations(processed_metadata)
    authors = build_authors(visualizations)
    name2author = {d["input"]: d for d in authors}

    with open(f"{output_dir}/authors.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(authors, indent=4, ensure_ascii=False))

    for d in visualizations:
        if d["authors"] is None:
            continue
        for i, name in enumerate(d["authors"]):
            if name in name2author:
                d["authors"][i] = name2author[name]["name"]

    with open(f"{output_dir}/visualizations.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(visualizations, indent=4, ensure_ascii=False))
