# DataCite Publication Scraper for The Alan Turing Institute

## Overview

This project aims to download and analyze publications that cite affiliation with "The Alan Turing Institute" from DataCite's API and other resources. Note that Zenodo and Arxiv both use DataCite as their DOI providers.

The project is implemented in Python and uses Poetry for dependency management.

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Contributing](#contributing)
6. [License](#license)
7. [Current status](#current-status)

## Prerequisites

- Python 3.x
- Poetry (for dependency management)

## Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/thealanturinginstitute/turing_publications.git
    ```

2. **Navigate to Project Directory**
    ```bash
    cd turing_publications
    ```

3. **Install Poetry**
    If you haven't installed Poetry yet, you can install it by following the instructions [here](https://python-poetry.org/docs/#installation).

4. **Install Dependencies**
    ```bash
    poetry install
    ```

## Usage

1. **Activate the Poetry Environment**
    ```bash
    poetry shell
    ```

2. **Run the Script**

    Download data from DataCite:
    ```bash
    python src/datacite_api.py
    ```

    Parse downloaded data into a csv file:
    ```bash
    python src/datacite2csv.py
    ```

## Contributing

If you would like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

MIT License. See [LICENSE](LICENSE) for details.


----------

## Current status

Downloading data from DataCite works by looking for "Alan Turing Institute" within the text of each record (different systems put affiliations into different places). This seems to download records largely from Zenodo.

Below I'm trying to collect some examples of outputs created by The Alan Turing Institute that are not included, for reference and debugging. This is biased and incomplete:

- Most of arxiv.org papers!
    - [Some papers from arxiv.org that include the Turing somewhere in the text](https://arxiv.org/search/?query=the+alan+turing+institute&searchtype=all&source=header)
    - [Random example from arxiv.org that came out of the Turing](https://arxiv.org/abs/1908.08737) where Turing is only listed as an affiliation in the actual paper
- Some Zenodo outputs:
    - [My Shiny workshop for AIM RSF](https://zenodo.org/record/7953445)
    - [AIM RSF outputs overall](https://zenodo.org/communities/ai-mltc-m/?page=1&size=20)
    - [REG illustrations](https://zenodo.org/record/7785796)
