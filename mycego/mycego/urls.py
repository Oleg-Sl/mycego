
from django.contrib import admin
from django.urls import path, include

from yadiskmanagerapp.views import GetSecretCodeView, GetTokenView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('auth/url', GetSecretCodeView.as_view(), name='auth_url'),
    path('auth/token', GetTokenView.as_view(), name='get_token'),
]
