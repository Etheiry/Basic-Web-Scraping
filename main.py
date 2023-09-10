from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)

htmlBytes = page.read()
html = htmlBytes.decode("utf-8")


def getTitle():
    titleIndex = html.find("<title>") + len("<title>")
    titleEndIndex = html.find("</title>")
    title = html[titleIndex:titleEndIndex]
    print(title)

print(html)

