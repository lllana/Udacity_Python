import pandas as pd

df = pd.read_csv("chicago.csv")
print(df.head())  # start by viewing the first few rows of the dataset!

print("describe: ", df.describe())

print(df.info())

print(df['User Type'].value_counts())

print("Null count:", df.isnull().sum().sum())