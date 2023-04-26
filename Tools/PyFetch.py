import requests
from github import Github

url1 = "https://raw.githubusercontent.com/Anupam1707/Python_Programmes/main/"
url2 = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/"
url3 = "https://raw.githubusercontent.com/Anupam1707/ai/main/"
url4 = "https://raw.githubusercontent.com/Anupam1707/food-sales-analysis/main/"

def python(name):
    page = requests.get(url1 + name)
    return page.text

def weather(name):
    page = requests.get(url2 + name)
    return page.text

def ai(name):
    page = requests.get(url3 + name)
    return page.text

def food(name):
    page = requests.get(url4 + name)
    return page.text
