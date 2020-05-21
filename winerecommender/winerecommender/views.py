from django.conf.urls import url
from django.shortcuts import render

from winerecommender import recommender

DEBUG = True
SECRET_KEY = 'f213e77e87be849fb0f13401c3030a5608fc7b7eb5b1cc508a9e867463c25f66'
ROOT_URLCONF = __name__


def home(request):
    likes = request.GET.getlist('likes')
    dislikes = request.GET.getlist('dislikes')
    ranking = recommender.rank(likes, dislikes)
    return render(request, 'results.html',
                  {'results': ranking,
                   'varieties': recommender.get_varieties(),
                   'likes': likes})


urlpatterns = [
    url(r'^$', home),
]
