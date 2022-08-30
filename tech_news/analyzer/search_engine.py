from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    filtered_news = search_news({"title": {"$regex": title, "$options": "i"}})
    return [(i["title"], i["url"]) for i in filtered_news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
