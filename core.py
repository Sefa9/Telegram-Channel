from urllib.request import  urlopen
import wikipedia as wiki
import json
import env


token = env.news_token
wiki.set_lang("tr")
news_sources = [
    'techradar',
    'techcrunch',
    'hacker-news',
    'ars-technica',
]
wiki_sources = [
    ''
]

def url(source,sortBy="top"):
    if sortBy == "":
        return "https://newsapi.org/v1/articles?source=" + source + "&apiKey=" + token
    return "https://newsapi.org/v1/articles?source=" + source + "&apiKey=" + token + "&sortBy=" + sortBy

class News:

    def __init__(self,source):
        self.source = source

    def getNews(self,which):
        data = json.loads(urlopen(url(self.source)).read().decode('utf-8').replace("'",'"'))
        if not data["status"] == "error":
            self.title = data["articles"].[which].["title"]
            self.description = data["articles"].[which].["description"]
            self.url = data["articles"].[which].["url"]

    def outputMessage(self,type):

        return """
        Haber kanalı: **{}**
        Günün manşeti: **{}**
        Açıklama: __{}__
        Bağlantı Linki: {}
        """.format(self.source.upper(),self.title,self.description,self.url)


class Wiki:

    def __init__(self,title):
        self.title = title

    def search(self,page):
        self.result = wiki.search(page).summary
        return """
        Sayfa: {},
        İçerik: {}
        """.format(self.title,self.result)

