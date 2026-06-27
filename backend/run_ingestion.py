from db.session import SessionLocal

from ingestion.rss_pipeline import ingest_feed

from trend_engine.snapshot_builder import build_daily_snapshot
from trend_engine.trend_detector import detect_trends

from reporting.growth_detector import detect_growth
from reporting.theme_detector import detect_themes
from reporting.theme_clustering import discover_themes

from datetime import date


RSS_FEEDS = [
    "https://feeds.feedburner.com/TechCrunch",
    "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
]


def run():

    db = SessionLocal()

    try:

        print("\n========== ATLAS INGESTION ==========\n")

        for feed in RSS_FEEDS:

            ingest_feed(
                feed,
                db
            )

        print("RSS ingestion complete.")

        snapshot = build_daily_snapshot(db)

        print(
            f"Snapshot created for {snapshot['snapshot_date']}"
        )

        growth = detect_growth(db)

        trends = detect_trends(
            db,
            date.today()
        )

        themes = detect_themes(db)

        discovered = discover_themes(db)

        print(
            f"Growth Signals : {len(growth)}"
        )

        print(
            f"Trend Signals  : {len(trends)}"
        )

        print(
            f"Themes         : {len(themes)}"
        )

        print(
            f"Clusters       : {len(discovered)}"
        )

        print("\n========== COMPLETE ==========\n")

    finally:

        db.close()


if __name__ == "__main__":
    run()