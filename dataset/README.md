# Dataset

This directory stores the code for building the old visualization dataset from the data sources.

## Project Structure

This directory is structured as:

```
📂dataset
 ┣ 📂output                     - a directory storing data files
 ┃ ┣ 📜authors.json             - the built dataset of "author" entities
 ┃ ┗ 📜visualizations.json      - the built dataset of "visualization" entities
 ┣ 📜_authors.py                - utility functions to build "author" entities
 ┣ 📜_loader.py                 - utility functions to load metadata
 ┣ 📜_visualizations.py         - utility functions to build "visualization" entities
 ┣ 📜build_dataset.py           - a script to build the dataset
 ┣ 📜README.md
 ┗ 📜summary-statistics.ipynb   - a notebook showing summary statistics
```
