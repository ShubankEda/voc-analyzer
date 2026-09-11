import pandas as pd

df = pd.read_csv("data/working/reviews.csv")
df["at"] = pd.to_datetime(df["at"])

# drop the 4 blank ones
df = df[df["content"].notna()]

# scope to 2023+
df = df[df["at"] >= "2023-01-01"]

# flag short reviews, don't delete them
df["word_count"] = df["content"].str.split().str.len()
df["is_short"] = df["word_count"] < 5

print("Reviews in scope:", len(df))
print("Substantive (5+ words):", (~df["is_short"]).sum())
print("\nVersion formats present:")
print(df["reviewCreatedVersion"].dropna().str[:4].value_counts().head())

df.to_csv("data/working/reviews_scoped.csv", index=False)

print("\n--- 20 random short reviews ---")
print(df[df["is_short"]]["content"].sample(20).to_string())

print("\n--- version prefix vs earliest date ---")
print(df.groupby(df["reviewCreatedVersion"].str[:4])["at"].min().sort_values())