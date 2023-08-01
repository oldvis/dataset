<a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
<a href="http://commitizen.github.io/cz-cli/">
    <img alt="Commitizen friendly" src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg">
</a>

# Old Visualization Dataset

A repository of historical visualization metadata and scripts for gathering metadata.

The dataset in this repository can be downloaded with [oldvis_dataset](https://github.com/oldvis/oldvis_dataset).

## Project Structure

- `./data-sources`: each subdirectory of it stores
    - the scripts for obtaining metadata and images from a data source
    - the obtained metadata and related cache
- `./dataset`: the main directory that stores
    - the scripts for processing the metadata in `./data-sources`
    - the processed metadata
