import pandas as pd
import matplotlib.pyplot as plt

file_path = "/Users/matsveitsiareshka/Code/hackathon/abfallkalender-wuerzburg.csv"

df = pd.read_csv(file_path, delimiter=";")

print(df.info())

print(df.head())

print(df.describe())

print(df.isnull().sum())
