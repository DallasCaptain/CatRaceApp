from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register/', views.register),
    path('login/', views.login),
    path('success/',views.success),
    path('logout/',views.logout),
    path('addCat/', views.addCat),
    path('removeCat/', views.removeCat),
    path('addRace/', views.addRace),
]