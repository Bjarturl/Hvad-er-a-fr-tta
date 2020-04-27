from collections import defaultdict, Counter
import random, os
import numpy as np
#https://nbviewer.jupyter.org/gist/yoavg/d76121dfde2618422139?fbclid=IwAR0k69malaRhpuulxJzKOsv_A_pnlIwwvdOYLnSsNkV3x-w_hVIG2kHYuDM
def generate_letter(model, history, order):
        history = history[-order:]
        dist = model[history]
        x = random.random()
        for c,v in dist:
            x = x - v
            if x <= 0: return c


def generate_text(model, order, nletters=1000):
    history = "~" * order
    out = []
    for _ in range(nletters):
        c = generate_letter(model, history, order)
        history = history[-order:] + c
        out.append(c)
    return "".join(out)



def train_char_model(fname, order, custom):
    if custom:
        data = fname
    else:
        with open(fname, encoding="utf-8") as f:
            data = f.read()
    model = defaultdict(Counter)
    pad = "~" * order
    data = pad + data
    for i in range(len(data)-order):
        history, char = data[i:i+order], data[i+order]
        model[history][char]+=1
    def normalize(counter):
        s = float(sum(counter.values()))
        return [(c,cnt/s) for c,cnt in counter.items()]
    outmodel = {hist:normalize(chars) for hist, chars in model.items()}
    return outmodel


def train_model(order, files):
    if type(files) == type(""):
        model = train_char_model(files, order, True)
    else:
        for filename in files:
            if "combined" not in filename:
                model = train_char_model("helpers/islendingasogur/files/" + filename, order, False)
    return model

def create_story(files, order, chapters, custom_story):
    if len(custom_story) >= 50:
        model = train_model(order, custom_story)
    else:
        model = train_model(order, files)
    try_again = True
    length = 100000
    text = [""]
    while try_again and length > 0:
        try:
            text = generate_text(model, order, length).split(". ")
            try_again = False
        except:
            length -= 50
    text.pop() #Remove potentially unfinished sentence at the end
    counter = 0 #Sentences
    chapter = 1
    story = ""
    while chapter <= chapters:
        try:
            story += ("\n{0}. kafli\n\n".format(chapter))
            chapter += 1
            for _ in range(random.randint(3, 5)):
                story += (". ".join(text[counter:counter+2]) + ".\n")
                counter += 3
        except:
            break
    return story

