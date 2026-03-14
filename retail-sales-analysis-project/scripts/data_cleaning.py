
import pandas as pd

df = pd.read_csv("../data/retail_sales_dataset.csv")

# remove duplicates
df = df.drop_duplicates()

# handle missing values
df = df.fillna(method="ffill")

print("Clean dataset shape:", df.shape)

df.to_csv("../data/retail_sales_cleaned.csv", index=False)
