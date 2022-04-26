from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Reviews, Rating, RatingStar


# class RatingForm(forms.ModelForm):
#     """Форма добавления рейтинга"""

#     start = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(),
#         widget=forms.RadioSelect(),
#         empty_label=None,
#     )

#     class Meta:
#         model = Rating
#         fields = ('star',)


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Reviews
        fields = ("text",)
    

class LoginForm(AuthenticationForm):
    """Форма авторизации пользователя"""

    username = forms.CharField(
        label='Имя', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class RegisterForm(UserCreationForm):
    """Форма регистрации пользователя"""

    username = forms.CharField(
        label='Имя пользователя', 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password1 = forms.CharField(
        label='Пароль', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля', 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalpha():
            raise ValidationError('Имя должно состоять из букв')
        return username
