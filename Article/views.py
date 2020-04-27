from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from helpers.newsGenerator import getRandomNews
from helpers.databaseNews import getRandomNewsFromDatabase
from helpers.islendingasogur.model import create_story
from concurrent.futures import ThreadPoolExecutor, wait
import logging, os
from pathlib import Path
logger = logging.Logger('catch_all')
# Create your views here.
def home(request):
    return render(request, 'Articles/index.html')

def newArticle(request):
    filters = dict(request.POST)
    filters.pop('csrfmiddlewaretoken')
    try:
        print("Fetching data from server..")
        data = getRandomNewsFromDatabase(filters)
        data["fromdb"] = 1
        print("Successfully fetched data from server")
    except Exception as e:
        logger.error(e, exc_info=True)
        print("Fetching data from server failed, reverting to backup")
        skip = True if filters['skip'][0] == "true" else False
        data = getRandomNews(skip)
        data["fromdb"] = 0
    return JsonResponse(data, safe=False)

def aboutUs(request):
     return render(request, 'Articles/hvaderadfretta.html')

def islendingasogur(request):
    stories = []
    for i in os.listdir('helpers/islendingasogur/files/'):
        if "combined" not in i:
            stories.append(i.split(".")[0].replace("_", " "))
    data = {"stories": stories}
    return render(request, 'Articles/islendingasogur.html', data)

def getIslendingasogur(request):
    order = int(request.POST['filters[accuracy]'])
    chapters = int(request.POST['filters[chapters]'])
    filename = request.POST['filters[story_base]'].replace(" ", "_") + ".txt"
    files = [filename]
    custom_story = request.POST['filters[custom_story]']
    #model_file = "helpers/islendingasogur/models/Njala.npy"
    story = create_story(files, order=order, chapters=chapters, custom_story=custom_story)
    story = story.replace("\n", "<br>")
    data = {"story": story}
    return JsonResponse(data, safe=False)




def topNews(request):
    imgs = []
    pathlist = Path("static/images/bestof").glob('**/*')
    for path in pathlist:
        # because path is object not string
        #imgs.append("/".join(str(path).replace("\\", "/").split("/")[1:]))
        imgs.append(str(path).replace("\\", "/"))
    return render(request, 'Articles/helstifrettum.html', {"imgs": imgs})