import csv
from datetime import date
from google_play_scraper import reviews, Sort

APP_ID = "com.samsara.driver"
OUTFILE = f"data/raw/samsara_driver_raw_{date.today()}.csv"

all_reviews = []
token = None
page = 0

while True:
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
    page += 1
    print(f"page {page} — total {len(all_reviews)}")

    # save as we go, so a crash at page 12 doesn't cost you pages 1-11
    with open(OUTFILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=all_reviews[0].keys())
        writer.writeheader()
        writer.writerows(all_reviews)

    if token is None:
        break

print(f"\nDone. {len(all_reviews)} reviews → {OUTFILE}")