import feedparser


def fetch_rss_feed(feed_url: str):
    feed = feedparser.parse(feed_url)

    articles = []

    for entry in feed.entries:

        articles.append(
            {
                "title": entry.get("title", ""),
                "content": entry.get("summary", ""),
                "url": entry.get("link", "")
            }
        )

    return articles