import requests
import pyjokes
import randfacts
import random


def getJoke():
    return pyjokes.get_joke()


def getQuote():
    # Inspirational Quotes By:
    # ZenQuotes API

    request = requests.get("https://zenquotes.io/api/random")
    request = request.json()
    request = request[0]

    quote = request.get("q")
    author = request.get("a")

    return quote, author


def getFact():
    return randfacts.get_fact()


def getUpdate():
    return "Version 3.4.0", "Added tracking of the put command."


def getNews(query):
  request = requests.get(f'https://newsapi.org/v2/everything?q="{query}"&language=en&sortBy=publishedAt&apiKey=0e2dea6255494e36b1460d53508b7b1e')

  request = request.json()
  
  article = request.get("articles")
  
  try:
    title = article[0].get("title")
    source = article[0].get("source").get("name")
    
    title = str(title) + " - " + str(source)
    text = article[0].get("description")
    url = article[0].get("url")
    img_url = article[0].get("urlToImage")
    times = article[0].get("publishedAt")

  except IndexError:
    return None, None, None, None, None, True

  return title, text, url, img_url, times, False
