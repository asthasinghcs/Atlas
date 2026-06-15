from db.session import SessionLocal

from ingestion.rss_pipeline import ingest_feed


TECHCRUNCH_RSS = (
    "https://feeds.feedburner.com/TechCrunch"
)


def run():

    db = SessionLocal()

    try:

        ingest_feed(
            TECHCRUNCH_RSS,
            db
        )

        print(
            "RSS ingestion completed."
        )

    finally:

        db.close()


if __name__ == "__main__":
    run()