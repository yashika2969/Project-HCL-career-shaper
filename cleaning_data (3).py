import pandas as pd

# 1. Load data
df = pd.read_csv("dataset_raw.csv")
print("Before cleaning:", df.shape)

# 2. Remove exact duplicate rows
df = df.drop_duplicates()

# 3. Fill missing numbers with the median (middle value)
df["Session_Duration_Mins"] = df["Session_Duration_Mins"].fillna(
    df["Session_Duration_Mins"].median()
)
df["User_Rating"] = df["User_Rating"].fillna(df["User_Rating"].median())

# 4. Convert Session_Date text into a real date format
df["Session_Date"] = pd.to_datetime(df["Session_Date"])

# 5. Save cleaned file
df.to_csv("dataset_cleaned.csv", index=False)
print("After cleaning:", df.shape)
print("Saved cleaned file to: dataset_cleaned.csv")
