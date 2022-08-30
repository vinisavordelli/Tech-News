import sys
from tech_news.analyzer.ratings import top_5_categories, top_5_news
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_tag,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def analyzer_menu():
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n"
    )
    function_by_option = {
        "0": populate_database_with_news,
        "1": show_news_by_title,
        "2": show_news_by_date,
        "3": show_news_by_tag,
        "4": show_news_by_category,
        "5": show_top_5_news,
        "6": show_top_5_categories,
        "7": show_exit_message,
    }
    if option in function_by_option:
        function_by_option[option]()
    else:
        print("Opção inválida", file=sys.stderr)


def populate_database_with_news():
    amount = int(input("Digite quantas notícias serão buscadas:"))
    get_tech_news(amount)


def show_news_by_title():
    title = input("Digite o título:")
    print(search_by_title(title))


def show_news_by_date():
    date = input("Digite a data no formato aaaa-mm-dd:")
    print(search_by_date(date))


def show_news_by_tag():
    tag = input("Digite a tag:")
    print(search_by_tag(tag))


def show_news_by_category():
    category = input("Digite a categoria:")
    print(search_by_category(category))


def show_top_5_news():
    print(top_5_news())


def show_top_5_categories():
    print(top_5_categories())


def show_exit_message():
    print("Encerrando script")
