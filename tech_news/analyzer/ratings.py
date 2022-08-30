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
    categories_occurrences_count = list(
        get_collection().aggregate(
            [
                {"$group": {"_id": "$category", "count": {"$sum": 1}}},
                {"$sort": {"count": -1, "_id": 1}},
                {"$limit": 5},
                {"$project": {"_id": 0, "name": "$_id"}},
            ]
        )
    )
    return [category["name"] for category in categories_occurrences_count]
