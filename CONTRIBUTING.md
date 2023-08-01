# Contributing

Thanks for being interested in contributing to this project!

## Development 

### Setup

Clone this repo to your local machine.
Make sure [poetry](https://python-poetry.org/) is installed on your machine.

Install the dependencies.

```bash
poetry install
```

## Contributing

### An enhancement that does not change the dataset

Feel free to enhance the existing functions and documentation.

### A change to the dataset

There are some notes on making changes to the dataset:

- To make a change to the dataset, you typically need to commit to multiple repositories in the [oldvis project](https://github.com/oldvis).
- Before you start working, it's better to open an issue to discuss first.

The following lists some common scenario and steps of making changes to the dataset.

#### Add a new data source

1. **Support data querying in libquery:** Add a `querier` to query metadata and images from the new data source.
    - **Where to place the `querier`:** If the data source is a widely used digital library with an official API, place the `querier` in [libquery](https://github.com/oldvis/libquery). Otherwise, place the `querier` in [libquery_extensions](https://github.com/oldvis/libquery_extensions).
    - **Example:** [The `querier` for David Rumsey Map Collection](https://github.com/oldvis/libquery/tree/main/libquery/david_rumsey_map_collection).
2. **Support data processing in libprocess:** Add a `processor` (that extends the `querier`) to process metadata.
    - **Where to place the `processor`:** If the `querier` has been placed in [libquery](https://github.com/oldvis/libquery) ([libquery_extensions](https://github.com/oldvis/libquery)), place the `processor` in [libprocess](https://github.com/oldvis/libprocess) ([libprocess_extensions](https://github.com/oldvis/libprocess)).
    - **Example:** [The `processor` for David Rumsey Map Collection](https://github.com/oldvis/libprocess/tree/main/libprocess/david_rumsey_map_collection).
3. **Add data querying and processing scripts to this repository**
    - **Where to place the scripts:** The scripts should be placed in a new subdirectory of `./data-sources/` of this repository.
    - **Example:** [The scripts for David Rumsey Map Collection](https://github.com/oldvis/dataset/tree/main/data-sources/david-rumsey-map-collection).
    - **Scripts to be added:** Please refer to the [README of `./data-sources/`](https://github.com/oldvis/dataset/blob/main/data-sources/README.md###subdirectory-scripts)
4. **Query metadata:** Execute `fetch_metadata.py` in  `./data-sources/{data-source-name}/` to query metadata.
5. **Query images:** Execute `fetch_images.py` in  `./data-sources/{data-source-name}/` to query images.
6. **Process metadata of unlabeled entries:** Execute `process_unlabeled_metadata.py` in  `./data-sources/{data-source-name}/`.
7. **Label unlabeled data:** Label unlabeled processed metadata entries in in `./data-sources/{data-source-name}/output/metadata-processed/unlabeled.json`.
    - **Which labeling tool to use:** You may use the [image classification labeler](https://github.com/oldvis/image-classification-labeler) in the oldvis project. Other image labeling tool may also serve the purpose, as long as the annotations are stored in the [`Annotation` data structure](https://github.com/oldvis/annotations/blob/main/image-classification/README.md##annotation-data-structure)
    - **Where to store the annotations:** The annotations should be stored in `./data-sources/{data-source-name}/output/annotations/annotations.json` of this repository. The annotations and the process for obtaining the annotations should also be stored in `./image-classification/{data-source-name}/` of [oldvis/annotations](https://github.com/oldvis/annotations) for reproducibility.
8. **Process metadata of visualizations:** Execute the data processing scripts.
    - **Scripts to be executed:** First, execute `process_vis_metadata.py` in `./data-sources/{data-source-name}/`. Then, execute `build_dataset.py` in `./dataset/`.

#### Add a new query to an existing data source

1. **Add a query:** Store add the query to `_queries.py` in  `./data-sources/{data-source-name}/`.
2. **Query metadata:** The same as for "Add a new data source".
3. **Process metadata of unlabeled entries:** The same as for "Add a new data source".
4. **Label unlabeled data:** Almost the same as for "Add a new data source", except that the obtained annotations need to be merged with the old annotations.
5. **Process metadata of visualizations:** The same as for "Add a new data source".

#### Re-run old queries to fetch data source update

1. **Query metadata:** The same as for "Add a new data source".
2. **Query images:** The same as for "Add a new data source".
3. **Process metadata of unlabeled entries:** The same as for "Add a new data source".
4. **Label unlabeled data:** Almost the same as for "Add a new data source", except that the obtained annotations need to be merged with the old annotations.
5. **Process metadata of visualizations:** The same as for "Add a new data source".

#### Update metadata processing

1. **Update data processing in libprocess:** Similar to "Support data processing in libprocess" for "Add a new data source", except that the `processor` should be edited instead of created from scratch.
2. **Process metadata of visualizations:** The same as for "Add a new data source".

#### Update annotations

1. **Edit annotations:** Similar to "Label unlabeled data" for "Add a new data source", except that the annotations should be edited instead of created from scratch.
3. **Process metadata of visualizations:** The same as for "Add a new data source".

## Code Style

Use [Black](https://github.com/psf/black) to detect code style issues and fix the issues before committing.

## Thanks

Thank you again for being interested in this project! You are awesome!
