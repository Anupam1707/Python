import requests
from github import Github

url1 = "https://raw.githubusercontent.com/Anupam1707/Python_Programmes/main/"
url2 = "https://raw.githubusercontent.com/Anupam1707/weather-app-py/main/"

def python(name):
    page = requests.get(url1 + name)
    return page.text

def weather(name):
    page = requests.get(url2 + name)
    return page.text
