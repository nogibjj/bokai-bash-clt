#!/usr/bin/env python

import click
import pandas as pd
from datetime import datetime

# build a click group
@click.group()
def cli():
    """A simple CLI to run different operations on dataset"""


# build a click command
@cli.command()
def describe():
    """Load the data and print the description in the terminal"""
    data = pd.read_csv("walmart-sales-dataset-of-45stores.csv").describe()
    print(data)


@cli.command()
@click.option("--store", default="1", help="Find all data of a specific store")
def find_store(store):
    """Find all data of a specific store"""
    data = pd.read_csv("walmart-sales-dataset-of-45stores.csv")
    print(data[data.Store == int(store)])


@cli.command()
@click.option("--y", default="2010", help="Year of the date, default 2010")
@click.option("--m", default="01", help="Month of the date, default 01")
@click.option("--d", default="01", help="Day of the date, default o1")
@click.option(
    "--b",
    default="1",
    help="Whether before the date or not, if 1 then before, otherwise after",
)
def find_date(y, m, d, b):
    """Find all data before or after a specific date"""

    data = pd.read_csv("walmart-sales-dataset-of-45stores.csv")
    data.Date = pd.to_datetime(data.Date)

    my_date_string = y + " " + m + " " + d
    dt = datetime.strptime(my_date_string, "%Y %m %d")
    if b == "1":
        print(data[data.Date < dt])
    else:
        print(data[data.Date > dt])


@cli.command()
@click.option(
    "--h", default="1", help="Whether a holiday. If 1 then holiday, if 0 not."
)
def holiday(h):
    """Find the data within/without the special holiday week."""
    data = pd.read_csv("walmart-sales-dataset-of-45stores.csv")
    print(data[data.Holiday_Flag == int(h)])


@cli.command()
@click.option(
    "--r", default="1", help="Index of row sorted by. If 1 then sort by the first row."
)
@click.option("--asc", default="1", help="If 1 then ascending, if 0 descending.")
def sort(r, asc):
    """Find the data within/without the special holiday week."""
    data = pd.read_csv("walmart-sales-dataset-of-45stores.csv")
    data.Date = pd.to_datetime(data.Date)
    col = list(data.columns)[int(r) - 1]
    flag = True if asc == "1" else False
    ans = data.sort_values(by=[col], ascending=flag)
    print(ans)


# run the CLI
if __name__ == "__main__":
    cli()
