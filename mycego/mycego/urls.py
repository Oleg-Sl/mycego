
from django.contrib import admin
from django.urls import path, include

from yadiskmanagerapp.views import get_file_list

urlpatterns = [
    path('', get_file_list, name='files'),
]
