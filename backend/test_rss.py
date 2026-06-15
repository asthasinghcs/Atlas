from ingestion.rss_ingestor import fetch_rss_feed


articles = fetch_rss_feed(
    "https://feeds.feedburner.com/TechCrunch"
)

print(f"Articles Found: {len(articles)}")

for article in articles[:5]:
    print()
    print(article["title"])