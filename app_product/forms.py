from .models import Product
from django import forms
from django.core import validators
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','price', 'type','img']


class AddForm(forms.Form):
    name = forms.CharField(max_length=50,label='Product Name',required=True)
    price = forms.IntegerField(label='Price Name')
    type = forms.ChoiceField(label='Price Name',choices=(('tv.','Tv'),
                                                   ('screen','Screen')))

class MyForm(forms.Form):
    name = forms.CharField(label='name')
    email = forms.EmailField(label='Email')
    ver_email = forms.EmailField(label='ver_email')
    message = forms.CharField(widget=forms.Textarea,label='Message',required=True,validators=[
        validators.MaxLengthValidator(10)
    ])

    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        ver_email = all_clean['ver_email']
        if email != ver_email :
            raise forms.ValidationError('Verfiy from your email')