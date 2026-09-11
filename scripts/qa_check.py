import pandas as pd

df = pd.read_csv("data/working/reviews.csv")

print("Rows:", len(df))
print("Unique review IDs:", df["reviewId"].nunique())
print("Duplicates:", len(df) - df["reviewId"].nunique())
print("-" * 40)

print("Blank review text:", df["content"].isna().sum())
print("Blank app version:", df["reviewCreatedVersion"].isna().sum())
print("-" * 40)

print("Star breakdown:")
print(df["score"].value_counts().sort_index())
print("-" * 40)

df["at"] = pd.to_datetime(df["at"])
print("Oldest:", df["at"].min())
print("Newest:", df["at"].max())
print("-" * 40)

print("Reviews per year:")
print(df["at"].dt.year.value_counts().sort_index())
print("-" * 40)

print("Top 10 app versions by review count:")
print(df["reviewCreatedVersion"].value_counts().head(10))
print("-" * 40)

df["word_count"] = df["content"].astype(str).str.split().str.len()
print("Median words per review:", df["word_count"].median())
print("Reviews under 5 words:", (df["word_count"] < 5).sum())