from urllib.request import urlopen
import re


def Target(url):
    websiteTarget = urlopen(url)
    targetBytes = websiteTarget.read()
    htmlCode = targetBytes.decode("utf-8")
    return htmlCode

def Search(pattern, code):
    search = re.search(pattern, code, re.IGNORECASE)
    search = search.group()
    ExtractTags(search)
   
def ExtractTags(searchResults):
    print(re.sub("<.*?>", "", searchResults))