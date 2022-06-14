from django.urls import path

from . import views
# from .views import api_home

urlpatterns = [
    path('', views.api_home), # localhost:8000/api/
    path('post', views.api_home_post)
]