import pandas as pd
df1 = pd.read_csv("data/lines_cleaned.csv")
df2 = pd.read_csv("data/stations_cleaned.csv")
df = pd.merge(df1, df2, on="line_cd", how="inner")
df = df[(df["company_cd"] >= 1) & (df["company_cd"] <= 6)]
df = df.to_csv("stations_cleaned_v2.csv", index=False)