
from django.contrib import admin
from django.urls import path, include

from yadiskmanagerapp.views import get_secret_code, get_secret_token, get_file_list

urlpatterns = [
    path('', get_file_list, name='files'),
    path('secret_code', get_secret_code, name='secret_code'),
    path('secret_token', get_secret_token, name='secret_token'),
]
