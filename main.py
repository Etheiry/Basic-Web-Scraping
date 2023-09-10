from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)

htmlBytes = page.read()
html = htmlBytes.decode("utf-8")


def patterns(options):

    if options == "title":
        getTitle()


def getTitle():
    titlePat = "<title.*?>.*?</title.*?>"
    
    results = re.search(titlePat, html, re.IGNORECASE)
    title = results.group()
    title = re.sub("<.*?>", "", title)

    print(title)

patterns("title")

