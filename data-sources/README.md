# Data Sources

This directory stores the scripts for obtaining raw data from a data source and the obtained raw data.

## Project Structure

### Directory

This directory is structured as:

```
📂data-sources
 ┣ 📂{data-source-name-1}
 ┣ 📂{data-source-name-2}
 ┣ 📂...
 ┣ 📜unzip_data.py          - a script to unzip all the data files
 ┗ 📜zip_data.py            - a script to zip all the data files
```

- **Usage of `unzip_data.py`**: Before carrying out data changes, the data files can be unzipped by `unzip_data.py`.
- **Usage of `zip_data.py`**: Before committing data changes, the data files should be zipped by `zip_data.py` to minimize their sizes.

### Subdirectory

Each subdirectory in this directory is structured as:

```
📂{data-source-name}
 ┣ 📂output                         - a directory storing data files
 ┃ ┣ 📂annotations
 ┃ ┃ ┣ 📜annotations.json           - image classification labels
 ┃ ┃ ┗ 📜README.md
 ┃ ┣ 📂imgs                         - fetched images (gitignored)
 ┃ ┃ ┣ 📜{uuid1}.{ext1}
 ┃ ┃ ┣ 📜{uuid2}.{ext2}
 ┃ ┃ ┗ 📜...
 ┃ ┣ 📂metadata
 ┃ ┃ ┗ 📜metadata.jsonl             - fetched metadata
 ┃ ┣ 📂metadata-processed
 ┃ ┃ ┣ 📜all.json                   - processed metadata of all the entries
 ┃ ┃ ┣ 📜all.zip                    - zipped processed metadata of all the entries
 ┃ ┃ ┣ 📜unlabeled.json             - processed metadata of unlabeled entries (gitignored)
 ┃ ┃ ┣ 📜unlabeled.zip              - zipped processed metadata of unlabeled entries (gitignored)
 ┃ ┃ ┣ 📜visualizations.json        - processed metadata of entries labeled as vis
 ┃ ┃ ┗ 📜visualizations.zip         - zipped processed metadata of entries labeled as vis
 ┃ ┗ 📜.gitignore
 ┣ 📜_querier.py                    - a package containing the querier instance
 ┣ 📜_queries.py                    - a package containing the queries to be conducted
 ┣ 📜fetch_images.py                - a script to fetch images
 ┣ 📜fetch_metadata.py              - a script to fetch metadata
 ┣ 📜process_all_metadata.py        - a script to process metadata of all the entries
 ┣ 📜process_unlabeled_metadata.py  - a script to process metadata of unlabeled entries
 ┣ 📜process_vis_metadata.py        - a script to process metadata of entries labeled as vis
 ┗ 📜README.md
```

### Subdirectory scripts

Each subdirectory contains Python scripts for maintaining the dataset.
Usage of scripts in each subdirectory:

- **Usage of `fetch_metadata.py`**: Fetch metadata and store them at `./output/metadata/metadata.jsonl`. Additional cache files may be created at `./output/metadata/query-return/`.
- **Usage of `fetch_images.py`**: Fetch images and store them at `./output/imgs/`. The images are fetched according to the metadata at `./output/metadata/metadata.jsonl`.
- **Usage of `process_unlabeled_metadata.py`**: Process the metadata entries at `./output/metadata/metadata.jsonl` that are unlabeled according to `./output/annotations/annotations.json`.
- **Usage of `process_vis_metadata.py`**: Process the metadata entries at `./output/metadata/metadata.jsonl` that are labeled as visualizations according to `./output/annotations/annotations.json`. The processing utilizes properties of corresponding images stored at `./output/imgs/`.
- **Usage of `process_all_metadata.py`**: Process all the metadata entries at `./output/metadata/metadata.jsonl`. This script mainly serves the debugging purpose.

A script can be executed with `poetry run python {script-name}.py`.
If the poetry virtual environment is already activated, a script can be executed directly with `python {script-name}.py`.
