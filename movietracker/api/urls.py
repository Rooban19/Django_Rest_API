from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet,RatingViewSet

router = routers.DefaultRouter()
router.register('movies',MovieViewSet,basename='movies')
router.register('ratings',RatingViewSet,basename='ratings')

urlpatterns = [
    path('', include(router.urls)),
]
 