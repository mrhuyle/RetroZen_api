from django.urls import path, include
from . import api

urlpatterns = [
    path('', api.post_list, name='post_list'),
    path('create/', api.post_create, name='post_create'),
    path('profile/<uuid:id>', api.post_list_profile, name='post_list_profile'),
]
