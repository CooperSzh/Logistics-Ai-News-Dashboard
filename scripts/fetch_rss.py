import feedparser
import json
from datetime import datetime

# 可替换为你自己的RSS源
RSS_FEEDS = [
    "https://www.customs.gov.hk/en/whats_new/rss.xml",
    "https://www.maritime-executive.com/rss",
    "https://shipping.einnews.com/rss.xml",
    "https://www.maritime-executive.com/rss",
    "https://www.marinelink.com/rss"
]

def parse_feed(url):
    feed = feedparser.parse(url)
    items = []

    for entry in feed.entries[:10]:
        items.append({
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "source": feed.feed.get("title", url),
        })

    return items

def main():
    all_news = []

    for rss in RSS_FEEDS:
        all_news.extend(parse_feed(rss))

    # 简单排序（按时间字符串）
    all_news = sorted(all_news, key=lambda x: x["published"], reverse=True)

    output = {
        "update_time": datetime.utcnow().isoformat(),
        "total": len(all_news),
        "data": all_news[:20]
    }

    with open("data/news.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
