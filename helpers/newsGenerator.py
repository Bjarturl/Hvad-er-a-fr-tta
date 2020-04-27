import markovify
import os, random, time

def getDataFromFile(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        header = f.read()
    data = None
    model = markovify.NewlineText(header, retain_original=False)
    while data == None:
        data = model.make_short_sentence(min_chars=40, max_chars=60)
    return data

def getRandomImage():
    with open("helpers/images.txt", 'r', encoding="utf-8") as f1:
        images = f1.read()
        images = images.split("\n")
    return random.choice(images)

def getArticle():
    with open("helpers/articles.txt", 'r', encoding="utf-8") as f1:
        content = f1.read().split("\n")
        #index = random.randint(0, len(content) - 3001)
        #content = content[index:index+3000]

    data = None
    while data == None:
        model = markovify.NewlineText(content, retain_original=False)
        data = model.make_sentence()
    return model.sentence_split(data)[0].split(". ")



def getRandomNews(skip):
    now = time.time()
    data = {
        "title": getDataFromFile("helpers/titles.txt"), 
        "article": "" if skip else getArticle(), 
        "caption": getDataFromFile("helpers/captions.txt"), 
        "image": getRandomImage(),
    }
    done = (int)(time.time() - now)
    data["time"] = done
    return data


