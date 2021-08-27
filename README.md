# Data Processing Challenge

A script to the Data Processing Challenge

### Decisions

To code the challenge I choose use pandas to work with the xlsx files. To populate the chart of accounts I used conditions and create new dataframes. For personal problems, time and knowledge I did not finish the challenge. But here is my ideas: to save the populated charts, I chose to use first a `.txt` file then change to a relational database like SQLite3, if the massive volume of data not much then 1GB, or PostgreSQL, to real massive volume of data.

## Summary

- [Installation](#installation)
- [Running Tests](#running-tests)
- [Documentation](#documentation)
- [Author](#author)

## Installation

Clone the project

```bash
  git clone https://github.com/fabiobarkoski/data-processing-challenge.git
```

Go to the project directory

```bash
  cd data-processing-challenge
```

Current to install the dependencies you need the package manager [Poetry](https://python-poetry.org/docs/). After installed type.

```bash
  poetry install
```

To start the App

```bash
  python -m path/to/script.py
```

## Running Tests

To run the tests, run the following command

```bash
  pytest
```

## Author

- [@fabiobarkoski](https://www.github.com/fabiobarkoski)