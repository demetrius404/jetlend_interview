import pandas as pd

# inn
# registration_date
# rating
# amount

df = pd.read_excel("example.xlsx")
df["registration_date"] = pd.to_datetime(df["registration_date"])
df["rating"] = df["rating"].astype("int")
df["amount"] = df["amount"].astype("float")
print(df)

# solution 1
df_lt_2021 = df[df["registration_date"] < "2021-01-01"]
print(df_lt_2021)
# output:
# 7700000098 1998-01-01 3 150.0
# 7700000001 2000-01-01 1 800.0

# solution 2
df_agg = df[["rating", "amount"]].groupby("rating").agg("sum")
print(df_agg)
# output:
# 1 900.0
# 2 140.0
# 3 130.0
