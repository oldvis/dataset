# Dataset

This directory stores the code for building the old visualization dataset from the data sources.

## Project Structure

This directory is structured as:

```
📂dataset
 ┣ 📂builders               - the Python package to build "author" and "visualization" entities
 ┣ 📂output                 - a directory storing data files
 ┃ ┣ 📜authors.json         - the built dataset of "author" entities
 ┃ ┗ 📜visualizations.json  - the built dataset of "visualization" entities
 ┣ 📂playground             - a directory storing preliminary data analysis results
 ┣ 📜_loader.py             - utility functions to load metadata
 ┣ 📜build_dataset.py       - a script to build the dataset
 ┗ 📜README.md
```
