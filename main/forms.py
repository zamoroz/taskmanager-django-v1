from django.forms import CharField, ModelForm, Textarea, TextInput, Select, PasswordInput, HiddenInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import task


class sign_in_form(AuthenticationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))

class sign_up_form(UserCreationForm):
    username = CharField(label='Имя пользователя', widget=TextInput(attrs={'class': 'form-control'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))
    password2 = CharField(label='Подтверждение пароля', widget=PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class task_form(ModelForm):
    user = HiddenInput()
    
    class Meta:
        model = task
        fields = ['title', 'task', 'status', 'user']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "status": Select(attrs={
                'class': 'from-select'
            }),
        }
