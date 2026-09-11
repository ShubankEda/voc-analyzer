from google_play_scraper import app, reviews, Sort

APP_ID = "com.samsara.driver"

# --- 1. How big is this app overall? ---
info = app(APP_ID, lang="en", country="us")
print("APP:", info["title"])
print("Average rating:", round(info["score"], 2))
print("Total ratings (all languages):", info["ratings"])
print("Total written reviews (all languages):", info["reviews"])
print("-" * 40)

# --- 2. Pull up to 1000 English/US reviews, page by page ---
all_reviews = []
token = None

while len(all_reviews) < 1000:
    batch, token = reviews(
        APP_ID,
        lang="en",
        country="us",
        sort=Sort.NEWEST,
        count=200,
        continuation_token=token,
    )
    if not batch:
        break
    all_reviews.extend(batch)
    print("fetched:", len(all_reviews))
    if token is None:
        break

print("-" * 40)
print("TOTAL EN/US PULLED:", len(all_reviews))

# --- 3. What does one review look like? ---
print("-" * 40)
print("SAMPLE RECORD:")
for key, value in all_reviews[0].items():
    print(f"  {key}: {value}")

# --- 4. How often is app version missing? ---
missing = sum(1 for r in all_reviews if not r["reviewCreatedVersion"])
print("-" * 40)
print(f"App version blank: {missing}/{len(all_reviews)} = {missing/len(all_reviews):.0%}")

# --- 5. Star breakdown ---
print("-" * 40)
for star in [1, 2, 3, 4, 5]:
    n = sum(1 for r in all_reviews if r["score"] == star)
    print(f"{star} star: {n}")

# --- 6. Date range ---
dates = sorted(r["at"] for r in all_reviews)
print("-" * 40)
print("Oldest:", dates[0])
print("Newest:", dates[-1])
