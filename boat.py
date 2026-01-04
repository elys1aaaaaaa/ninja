import pandas as pd
df = pd.read_csv("./titanic/train.csv")

#pd.set_option('display.max_columns', None)
#pd.set_option("display.max_rows", 8)

pd.set_optiom("max_colwidth, None")
print(titanic[["Name", "Fare"]].head())

print(df.head())