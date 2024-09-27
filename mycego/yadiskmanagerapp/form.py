from django import forms


class ClientDataForm(forms.Form):
    client_id = forms.CharField(max_length=255)
    client_secret = forms.CharField(max_length=255)


class CodeForm(forms.Form):
    code = forms.IntegerField()


class PublicUrlForm(forms.Form):
    url = forms.CharField(max_length=255)
