from django.shortcuts import render, redirect
from requests_oauthlib import OAuth2Session

from .form import PublicUrlForm, ClientDataForm, CodeForm


def get_secret_code(requests):
    if requests.method == 'POST':
        form = ClientDataForm(requests.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            client_id = form_data.get('client_id')
            client_secret = form_data.get('client_secret')
            response = redicrect('secret_token')
            response.set_cookie(key='client_id', value=client_id)
            response.set_cookie(key='client_secret', value=client_secret)
            return response

    form = ClientDataForm()
    response = render(requests, 'yadiskmanagerapp/secret_code.html', {'form': form})
    return response

def get_secret_token(requests):
    if requests.method == 'POST':
        form = CodeForm(requests.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            client_id = form_data.get('client_id')
            client_secret = form_data.get('client_secret')
            response = render(requests, 'yadiskmanagerapp/index.html', {'form': form})
            response.set_cookie(key='client_id', value=client_id)
    else:
        form = CodeForm()
        response = render(requests, 'yadiskmanagerapp/index.html', {'form': form})

    return response


def get_file_list(requests):
    return redirect('secret_code')
    # if requests.method == 'POST':
    #     form = PublicUrlForm(requests.POST)
    #     if form.is_valid():
    #         form_data = form.cleaned_data
    #         print("Form data: ", form_data)
    #         public_url = form_data.get('url')
    # else:
    #     form = PublicUrlForm()
    
    # response = render(requests, 'yadiskmanagerapp/index.html', {'form': form})

    # return response
