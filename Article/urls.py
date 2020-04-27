from django.urls import path
from Article import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newArticle", views.newArticle),
    path("hvaderadfretta", views.aboutUs),
    path("helstifrettum", views.topNews),
    path("sogur", views.islendingasogur),
    path("getIslendingasogur", views.getIslendingasogur),

]