from django import forms


class ClientDataForm(forms.Form):
    client_id = forms.CharField(label='Client ID', max_length=255)
    client_secret = forms.CharField(label='Client Secret', max_length=255)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class CodeForm(forms.Form):
    code = forms.IntegerField(label='Код доступа')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class PublicUrlForm(forms.Form):
    url = forms.CharField(label='Ключ опубликованного ресурса или публичная ссылка на ресурс', max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
