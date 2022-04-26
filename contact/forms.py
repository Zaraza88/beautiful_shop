from django import forms
from .models import ContactModel
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class FormContact(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = ContactModel
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalpha():
            raise ValidationError('Имя должно состоять из букв')
        return username


    