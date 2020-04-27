from bs4 import BeautifulSoup as bs
import urllib.request
import csv, os, markovify

url = "https://www.snerpa.is/net/isl/isl.htm"
page = urllib.request.urlopen(url)

mainParse = bs(page, 'lxml')
for a in mainParse.findAll("a", href=True):
    if "index" not in a['href']:
        link = "https://www.snerpa.is/net/isl" + a['href'][1:]
# url = "https://www.snerpa.is/net/isl/gisl.htm"
        print(link)
        page = urllib.request.urlopen(link)
        parse = bs(page, 'lxml')
        title = parse.findAll("title")[0].text.replace(" ", "_") + ".txt"
        story = ""
        for p in parse.findAll("p", text=True):
            sentences = p.text.replace("\r", "").replace("\n", "").strip().split(" ")

            for s in sentences:

                if s != "":
                    stripped_sentence = " ".join([word for word in s.split(" ") if word != ""]) + " "
                    story += stripped_sentence
        with open(title, 'w+', encoding="utf-8") as f:
            f.write(story)