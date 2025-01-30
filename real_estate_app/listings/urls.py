
from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.listings, name='all-properties'),
    path('land/', views.land_list, name='land'),
    path('houses/', views.houses_list, name='houses'),
]
