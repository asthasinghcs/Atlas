from db.session import SessionLocal

from ingestion.rss_pipeline import ingest_feed


RSS_FEEDS = [
    "https://feeds.feedburner.com/TechCrunch",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]


def run():

    db = SessionLocal()

    try:

        for feed in RSS_FEEDS:

            ingest_feed(
                feed,
                db
            )

        print(
            "RSS ingestion completed."
        )

    finally:

        db.close()


if __name__ == "__main__":
    run()