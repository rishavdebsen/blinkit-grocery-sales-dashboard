"""Exploratory analysis of the BlinkIT grocery dataset.

Companion script for the Power BI dashboard in this repository. Computes
aggregate metrics and breakdowns from the dataset.

Dataset: BlinkIT Grocery Data (practice dataset shared by the Data Tutorials
YouTube walkthrough), 8,523 rows. Download it from the tutorial's data folder
and place the file next to this script.
Usage:  pip install pandas openpyxl
        python blinkit_eda.py
"""

import pandas as pd

DATA = "BlinkIT Grocery Data.xlsx"


def load_data(path: str = DATA) -> pd.DataFrame:
    df = pd.read_excel(path)
    # Standardise the inconsistent fat-content labels in the raw file.
    df["Item Fat Content"] = df["Item Fat Content"].replace(
        {"low fat": "Low Fat", "LF": "Low Fat", "reg": "Regular"}
    )
    return df


def headline_numbers(df: pd.DataFrame) -> None:
    print("=== Headline numbers ===")
    print(f"Item-outlet rows:         {len(df):,}")
    print(f"Total sales:              {df['Sales'].sum():,.2f}")
    print(f"Average sales per item:   {df['Sales'].mean():,.2f}")
    print(f"Average rating:           {df['Rating'].mean():.2f}")
    print(f"Unique items:             {df['Item Identifier'].nunique():,}")
    print(f"Outlets:                  {df['Outlet Identifier'].nunique()}")


def breakdowns(df: pd.DataFrame) -> None:
    print("\n=== Sales by item fat content ===")
    print(df.groupby("Item Fat Content")["Sales"].sum().round(2))

    print("\n=== Top 5 item types by sales ===")
    print(df.groupby("Item Type")["Sales"].sum().sort_values(ascending=False).head(5).round(2))

    print("\n=== Sales by outlet location type ===")
    print(df.groupby("Outlet Location Type")["Sales"].sum().round(2))

    print("\n=== Sales by outlet size ===")
    print(df.groupby("Outlet Size")["Sales"].sum().round(2))

    print("\n=== Sales by outlet establishment year ===")
    print(df.groupby("Outlet Establishment Year")["Sales"].sum().round(2))


if __name__ == "__main__":
    data = load_data()
    headline_numbers(data)
    breakdowns(data)
