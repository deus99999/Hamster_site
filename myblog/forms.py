from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Post
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select, FileInput, HiddenInput


class ContactForm(forms.Form):
    # from_email = forms.EmailField(label='Email',
    #                             widget=forms.TextInput(attrs={"class": "form-control",
    #                                                           "placeholder": "Ваш Email"}),
    #                               required=True)
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={"class": "form-control",
                                                                'cols': 50, 'rows': 15,
                                                              "placeholder": "Текст сообщения"}),
                              required=True)


class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'url']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название"}),
            "image": FileInput(attrs={
                "class": "form-control"}),
            "content": Textarea(attrs={
                "class": "form-control",
                'cols': 50, 'rows': 20,
                "placeholder": "Текст статьи"}),
            }


class SigUpForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "inputUsername",
            'placeholder': "Ваше имя"
        }),
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
            'placeholder': "Пароль"
        }),
    )
    repeat_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "ReInputPassword",
            'placeholder': "Повторите пароль"
        }),
    )

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repeat_password']

        if password != confirm_password:
            raise forms.ValidationError(
                "Пароли не совпадают"
            )

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
        )


class SignInForm(forms.Form):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': "InputUsername"
        })
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': "form-control",
            'id': "inputPassword",
        })
    )