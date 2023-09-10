import scrap as scrap



pat = "<.*?>Name:.*?</.*?>"


html = scrap.Target("http://olympus.realpython.org/profiles/dionysus")
scrap.Search(pat, html)


