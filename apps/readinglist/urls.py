from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'readinglist'

router = routers.DefaultRouter()
router.register('', views.ReadingListViewSet, basename='listas_leitura')

urlpatterns = [
    path('', include(router.urls) )
]