import requests
from time import sleep
from http import HTTPStatus
from parsel import Selector


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )

        if response.status_code == HTTPStatus.OK:
            return response.text
        else:
            return None
    except Exception as e:
        print(e)
        return None
    finally:
        sleep(1)


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    urls = selector.css(".archive-main .entry-title a::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_link = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    return {
        "url": selector.css('link[rel="canonical"]::attr(href)').get(),
        "title": selector.css(".entry-title::text").get().strip(),
        "timestamp": selector.css(".meta-date::text").get(),
        "writer": selector.css(".meta-author .author a::text").get(),
        "comments_count": len(selector.css(".comment-body").getall()),
        "summary": selector.xpath('string(//div[@class="entry-content"]//p)')
        .get()
        .strip(),
        "tags": selector.css('.post-tags [rel="tag"]::text').getall(),
        "category": selector.css(".meta-category .label::text").get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
