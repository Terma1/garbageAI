import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, HTML
import scipy.stats as stats

file_path = "/Users/matsveitsiareshka/Code/hackathon/abfallkalender-wuerzburg.csv"

df = pd.read_csv(file_path, delimiter=";")

print(df.info())

print(df.head())

print(df.describe())

print(df.isnull().sum())
if "Stadtteil" in df.columns:
    print("\nКоличество уникальных районов (Stadtteil):", df["Stadtteil"].nunique())
    print("\nСписок районов:")
    print(df["Stadtteil"].unique())

if "bild" in df.columns and "kategorie" in df.columns:
    print("")
    duplicates = df.groupby("bild")["kategorie"].nunique()
    if (duplicates > 1).any():
        print("")
        print(duplicates[duplicates > 1])
    else:
        print("")

date_list = df.groupby("Stadtteil")["Datum"].apply(lambda x: sorted(x.unique()))
if "Stadtteil" in df.columns and "Datum" in df.columns:
    date_counts = df.groupby("kategorie")[["Stadtteil","Datum"]].nunique()

    dates_multiple_areas = date_counts[date_counts > 1]
    
    print(dates_multiple_areas)