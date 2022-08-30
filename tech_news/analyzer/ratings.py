from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    filtered_news = list(
        get_collection()
        .find({}, {"_id": False})
        .sort([("comments_count", -1), ("title", 1)])
        .limit(5)
    )
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
