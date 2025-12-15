#! /usr/bin/env -S uv run --script --managed-python --python=3.14.2
""" Read airports.csv, filter North American open airports, and write the result.

This module reads 'airports.csv' with pandas, treats empty elevation_ft values as
NA, filters rows where continent == "NA" and type != "closed", and writes the
filtered DataFrame to 'airports-na-open.csv'.
"""

# /// script
# dependencies = [
#   "pandas",
# ]
# ///
import pandas as pd


def main() -> None:
    """ Read airports.csv, filter North American open airports, and write the result.

    This function reads 'airports.csv' while treating empty elevation_ft values
    as NA, filters rows where continent == "NA" and type != "closed", and writes
    the filtered DataFrame to 'airports-na-open.csv'.
    """

    na = {
        "elevation_ft": [""],  # uses float64 instead of object/string
    }
    df = pd.read_csv("airports.csv",
                       keep_default_na=False,
                       na_values=na,
            )
    # df.info()

    filtered = df[
        (df["continent"] == "NA")
        &
        (df["type"] != "closed")
    ]
    # filtered.info()
    filtered.to_csv("airports-na-open.csv", index=False)


if __name__ == "__main__":
    main()
