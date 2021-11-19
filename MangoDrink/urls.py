from django.urls import path
from MangoDrink import views
from Mango import urls

app_name = 'MangoDrink'
urlpatterns = [
    path('', views.index, name='index'),
    path('other', views.other, name='other'),
    path('information', views.information, name='information'),
]
