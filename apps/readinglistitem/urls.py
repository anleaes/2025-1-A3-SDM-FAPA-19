from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'readinglistitem'

router = routers.DefaultRouter()
router.register('', views.ReadingListItemViewSet, basename='itens_lista_leitura')

urlpatterns = [
    path('', include(router.urls) )
]