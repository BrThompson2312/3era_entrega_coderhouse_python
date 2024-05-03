from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from AppBlogger.models import Blog, Message

class FormularioBlog(forms.Form):
    titulo = forms.CharField(max_length=30)
    subtitulo = forms.CharField(max_length=30)
    cuerpo = forms.CharField(max_length=1000)
    autor = User
    fecha = forms.DateField()
    imagen = forms.ImageField(label="Imagen", required=False)
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'fecha', 'imagen']

class FormularioMessage(forms.Form):
    username = User
    message = forms.CharField(max_length=200)
    class Meta:
        model = Message
        fields = ['username', 'message']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen = forms.ImageField(label="Avatar", required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'imagen']
        help_text = {k:"" for k in fields}

class UserEditForm(UserChangeForm):
    imagen = forms.ImageField(label="Avatar", required=False)
    username = forms.CharField(label="Nombre")
    email = forms.EmailField(label="Ingrese su email")
    password = None
    class Meta:
        model = User
        fields = ['imagen', 'username', 'email']
        help_text = {k:"" for k in fields}

class BloggerEditForm(UserCreationForm):
    email = forms.EmailField(label="Ingrese su email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    username = forms.CharField(max_length=30)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'username']
        help_text = {k:"" for k in fields}