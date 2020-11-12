from urllib.request import urlopen

url = "https://www.espn.com/soccer/scoreboard?league=eng.1"

page = urlopen(url)

page

html_bytes = page.read()
html = html_bytes.decode("utf-8")

f = open("test.txt", "a")
f.write(html)
f.close()
