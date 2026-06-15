import feedparser
from bs4 import BeautifulSoup


def fetch_rss_feed(feed_url: str):
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:

        raw_content = entry.get(
            "summary",
            ""
        )

        clean_content = (
            BeautifulSoup(
                raw_content,
                "html.parser"
            )
            .get_text(
                separator=" ",
                strip=True
            )
        )

        articles.append(
            {
                "title": entry.get("title", ""),
                "content": clean_content,
                "url": entry.get("link", "")
            }
        )

    return articles