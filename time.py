import pandas as pd


file_path = "/Users/matsveitsiareshka/Code/hackathon/abfallkalender-wuerzburg.csv"

df = pd.read_csv(file_path, delimiter=";")

df['Datum'] = pd.to_datetime(df['Datum'])


df = df[df['Datum'].dt.month != 1]

df = df.sort_values(by=['kategorie', 'Stadtteil', 'Datum'])

df['DateDiff'] = df.groupby(['kategorie', 'Stadtteil'])['Datum'].diff().dt.days

average_lifespan_by_area = df.groupby(['kategorie', 'Stadtteil'])['DateDiff'].mean()

print("\nСредний промежуток между днями вывоза для каждой категории мусора в каждом районе:")
print(average_lifespan_by_area)
