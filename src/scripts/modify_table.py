import pandas as pd

df = pd.read_csv("table.csv")

drop_columns = ["Website",	"View Certificate",	"Details",	"Map"]
df.drop(drop_columns, axis=1, inplace=True)

df.to_csv("table_modified.csv")