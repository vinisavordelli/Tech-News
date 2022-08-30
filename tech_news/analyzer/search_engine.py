from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    filtered_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 7
def search_by_date(date):
    try:
        formated_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        filtered_news = search_news({"timestamp": formated_date})
        return [(news["title"], news["url"]) for news in filtered_news]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    filtered_news = search_news({"tags": {"$regex": tag, "$options": "i"}})
    return [(news["title"], news["url"]) for news in filtered_news]


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    return [(news["title"], news["url"]) for news in news]
