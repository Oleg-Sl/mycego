from django.shortcuts import render, redirect
from django.views import View
from requests_oauthlib import OAuth2Session

from .form import PublicUrlForm, ClientDataForm, CodeForm
from .services.token_utils import get_token, get_authorization_url
from .services.yadisk_api import YaDiskAPI
from .configs.yadisk_file_types import YADISK_FILE_TYPES


class GetSecretCodeView(View):
    def get(self, request):
        form = ClientDataForm()
        return render(request, 'yadiskmanagerapp/auth_url.html', {'form': form})

    def post(self, request):
        form = ClientDataForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            client_id = form_data.get('client_id')
            client_secret = form_data.get('client_secret')
            authorization_url = get_authorization_url(client_id)

            response = redirect('get_token')
            response.set_cookie(key='client_id', value=client_id)
            response.set_cookie(key='client_secret', value=client_secret)
            response.set_cookie(key='authorization_url', value=authorization_url)
            return response

        return render(request, 'yadiskmanagerapp/auth_url.html', {'form': form})

class GetTokenView(View):
    def get(self, request):
        form = CodeForm()
        authorization_url = request.COOKIES.get('authorization_url')
        return render(request, 'yadiskmanagerapp/get_token.html', {'form': form, 'authorization_url': authorization_url})

    def post(self, request):
        form = CodeForm(request.POST)
        authorization_url = request.COOKIES.get('authorization_url')

        if form.is_valid():
            form_data = form.cleaned_data
            code = form_data.get('code')
            client_id = request.COOKIES.get('client_id')
            client_secret = request.COOKIES.get('client_secret')

            if not client_id or not client_secret:
                return render(request, 'yadiskmanagerapp/get_token.html', {'form': form, 'error': "Не удалось получить client_id или client_secret."})

            try:
                token = get_token(client_id, client_secret, code)
            except Exception as e:
                authorization_url = request.COOKIES.get('authorization_url')
                return render(request, 'yadiskmanagerapp/get_token.html', {'form': form, 'authorization_url': authorization_url, 'error': str(e)})

            response = redirect('index')
            response.set_cookie(key='token', value=token)
            return response

        return render(request, 'yadiskmanagerapp/get_token.html', {'form': form})


class IndexView(View):
    def get(self, request):
        token = request.COOKIES.get('token')
        if token is None:
            return redirect('auth_url')

        form = PublicUrlForm()
        return render(request, 'yadiskmanagerapp/index.html', {'form': form, 'files': [], 'file_types': YADISK_FILE_TYPES})

    def post(self, request):
        token = request.COOKIES.get('token')
        if token is None:
            return redirect('auth_url')

        form = PublicUrlForm(request.POST)
        if form.is_valid():
            file_type = request.POST.get('file_type')
            form_data = form.cleaned_data
            public_url = form_data.get('url')

            ya_disk_api = YaDiskAPI(token)
            result, status = ya_disk_api.get_public_resources(public_url)
            if not status:
                return render(request, 'yadiskmanagerapp/index.html', {'form': form, 'files': [], 'file_types': YADISK_FILE_TYPES, 'error': result.get('message')})
            
            data_files = result.get('_embedded', {}).get('items', [])
            filter_data_files = [file for file in data_files if not file_type or file.get('media_type') == file_type]
            return render(request, 'yadiskmanagerapp/index.html', {'form': form, 'files': filter_data_files, 'file_types': YADISK_FILE_TYPES})

        return render(request, 'yadiskmanagerapp/index.html', {'form': form, 'files': [], 'file_types': YADISK_FILE_TYPES})
