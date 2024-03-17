import requests
from bs4 import BeautifulSoup

class News:
    """
    A class to interact with a news API and fetch news articles based on specified criteria.

    Attributes:
        api_key (str): The API key used to authenticate with the news API.
        url (str): The endpoint URL of the news API.
        query (str): The search query used to filter news articles.
        country (str): The country code (ISO 3166-1 alpha-2) for filtering articles by country.
        article_count (int): The number of articles to fetch.
        search_lang (str): The language code (ISO 639-1) for filtering articles by language.
        spellcheck (int): Flag to enable/disable spellcheck (default: 1, enabled).
    """

    def __init__(self, api_key, url, query, country, article_count, search_lang) -> None:
        """
        Initializes the News class with the provided parameters.

        Args:
            api_key (str): The API key used to authenticate with the news API.
            url (str): The endpoint URL of the news API.
            query (str): The search query used to filter news articles.
            country (str): The country code (ISO 3166-1 alpha-2) for filtering articles by country.
            article_count (int): The number of articles to fetch.
            search_lang (str): The language code (ISO 639-1) for filtering articles by language.
        """
        self.api_key = api_key
        self.url = url
        self.query = query
        self.country = country
        self.count = article_count
        self.search_lang = search_lang
        self.spellcheck = 1

    @staticmethod
    def fetch_article_content(url):
        """
        Fetches the content of a news article from a given URL.

        Args:
            url (str): The URL of the news article.

        Returns:
            str: The text content of the news article, or None if fetching failed.
        """
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Extract text content from the parsed HTML
                text_content = ' '.join([p.get_text() for p in soup.find_all('p')])
                return text_content
            else:
                print(f"Failed to fetch content for URL: {url}. Status code: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred while fetching content for URL: {url}. Error: {str(e)}")
            return None

    def fetch_news(self):
        """
        Fetches news articles based on the specified criteria.

        Returns:
            str: A formatted string containing information about the fetched news articles.
        """
        headers = {
            "Accept": "application/json",
            "Accept-Encoding": "gzip",
            "X-Subscription-Token": self.api_key
        }
        params = {
            "q": self.query,
            "count": self.count,
            "country": self.country,
            "search_lang": self.search_lang,
            "spellcheck": self.spellcheck
        }
        response = requests.get(self.url, params=params, headers=headers)
        if response.status_code == 200:
            news_data = response.json()
            for item in news_data.get('results', []):
                article_url = item.get('url')
                if article_url:
                    content = self.fetch_article_content(article_url)
                    item['content'] = content
            return item['content']
        else:
            print(f"Failed to fetch news data. Status code: {response.status_code}")
            return None

# Example usage
# url = f"https://api.search.brave.com/res/v1/news/search"
# api_key = "Your Key"
# query = "india"
# news_data = News(url=url, api_key= api_key, query=query, country="us", article_count=2, search_lang="en")
# print(news_data.fetch_news())
