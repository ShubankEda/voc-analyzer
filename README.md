# Voice-of-Customer Analyzer

Categorizing driver complaints from public Google Play reviews,
with a hand-labeled evaluation set to measure classification accuracy.

## Data

Source: Google Play, Samsara Driver (`com.samsara.driver`), en/US.
Pulled 2026-09-10. 4,303 reviews, zero duplicate IDs, spanning
Oct 2016 to Sep 2026.

Scoped to 2023-01-01 onward: 1,780 reviews, of which 1,064 are
substantive (5+ words). Earlier reviews describe a product that has
changed substantially and would distort trend analysis.

## Known limitations

- **Written reviews only.** The store shows ~24,700 ratings against
  ~4,100 written reviews. This dataset reflects users motivated enough
  to type, which skews negative. Findings describe vocal drivers,
  not the average driver.
- **Short reviews skew positive.** 40% of in-scope reviews are under
  five words and are overwhelmingly praise ("Great", "Good app").
  Filtering to substantive reviews therefore over-represents complaints.
  Short reviews are flagged, not deleted — they still count for sentiment.
- **Version scheme is year+quarter** (2310 = 2023 Q1, 2410 = 2024 Q1).
  Entries below 2310 are drivers on old builds reviewing in 2023, not
  2023 releases. Excluded from version-based trends.
- **App version missing on ~8.7%** of rows.
- Play Store's headline review count did not match what pagination
  returned. Used the paged count.

## Open question

Release cadence increased sharply — four releases in 2023, ten by
August 2026. Worth testing whether stability complaints track that.

## Structure

data/raw/       immutable snapshot, read-only
data/working/   working copies, safe to overwrite
scripts/        pull, QA, scoping
logs/           raw LLM responses (Session 5 onward)