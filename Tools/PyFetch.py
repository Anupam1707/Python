import requests

url1 = "https://raw.githubusercontent.com/Anupam1707/Python/main/"
url2 = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/"
url3 = "https://raw.githubusercontent.com/Anupam1707/ai/main/main.py"

def python(name):
    page = requests.get(url1 + name)
    return page.text

def weather(name):
    page = requests.get(url2 + name)
    return page.text

def ai():
    page = requests.get(url3)
    return page.text
