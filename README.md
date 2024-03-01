# AI-Powered Text Generation with OpenAI

████████╗██████╗ ███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ██╗███████╗██╗      █████╗ ███╗   ██╗██████╗ 
╚══██╔══╝██╔══██╗██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ██║██╔════╝██║     ██╔══██╗████╗  ██║██╔══██╗
   ██║   ██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██║███████╗██║     ███████║██╔██╗ ██║██║  ██║
   ██║   ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚════██║██║     ██╔══██║██║╚██╗██║██║  ██║
   ██║   ██║  ██║███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║███████║███████╗██║  ██║██║ ╚████║██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ 

This repository contains classes for interacting with news APIs and generating text using the OpenAI API.


### News Class

#### How to Use

1. Install the `newsdataapi` Python package:

    ```bash
    pip install newsdataapi
    ```

2. Obtain an API key from the news service provider.

3. Initialize the `News` class with your API key:

    ```python
    from newsdataapi import NewsDataApiClient
    from news import News

    # Initialize the News class with your API key
    news = News(API_KEY=your_api_key)
    ```

4. Use the `get_articles` method to retrieve articles based on your criteria:

    ```python
    # Retrieve and print articles based on the specified query, country, and language
    print(news.get_articles(query="ronaldo", country="us", lan="en"))
    ```

#### Parameters

- `query` (str): The search query used to filter articles.
- `country` (str): The country code (ISO 3166-1 alpha-2) for filtering articles by country.
- `lan` (str): The language code (ISO 639-1) for filtering articles by language.

#### Returns

- `str`: A formatted string containing information about the retrieved articles.

---

### GP_Generate Class

#### How to Use

1. Install the `openai` Python package:

    ```bash
    pip install openai
    ```

2. Obtain an API key from OpenAI.

3. Initialize the `GP_Generate` class with your API key:

    ```python
    from openai import OpenAI
    from gp_generate import GP_Generate

    # Initialize the GP_Generate class with your API key
    generator = GP_Generate(api_key=your_api_key)
    ```

4. Use the `ask` method to generate text based on user queries:

    ```python
    # Generate text based on user queries
    result = generator.ask()
    print(result)
    ```

#### Parameters

- None

#### Returns

- `str`: The generated text containing answers to user queries.

These README files provide users with instructions on how to use the respective classes and their methods. Adjust `your_api_key` with your actual API key when using these classes.