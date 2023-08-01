"""
The script to construct a collection of "visualization" and "author" entities from the metadata.
The metadata of multiple data sources are combined.

Side effects of this script:
- The visualizations will be stored in "visualizations.json".
- The authors will be stored in "authors.json".
"""

import json
import os

from _authors import build_authors
from _loader import load_processed_metadata
from _visualizations import build_visualizations


if __name__ == "__main__":
    output_dir = "./output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    dataset_names = [
        "alabama-maps",
        "british-library-collection-items",
        "british-library-images-online",
        "david-rumsey-map-collection",
        "gallica",
        "internet-archive",
        "library-of-congress",
        "telefact",
    ]
    processed_metadata = load_processed_metadata(dataset_names=dataset_names)

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
        f.write(json.dumps(visualizations, indent=4))
