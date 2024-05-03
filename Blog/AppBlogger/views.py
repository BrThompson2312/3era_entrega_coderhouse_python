from django.shortcuts import render, redirect
from AppBlogger.models import Blog, Message
from AppBlogger.forms import UserEditForm, BloggerEditForm, FormularioBlog, FormularioMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

@login_required
def view_app(request):
    blog = Blog.objects.all()
    contexto = {"Blogs":blog}
    return render(request, "AppBlogger/blogs.html", contexto)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user is not None:
                login(request, user)
                return redirect("Pages")            
            else: 
                return render(request,"AppBlogger/login.html", {"mensaje":"Error, datos incorrectos"} )
        else:
            form = AuthenticationForm()
            return render(request,"AppBlogger/login.html", {'form':form, 'mensaje': "Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,"AppBlogger/login.html", {'form':form})

def register_request(request):
    if request.method == 'POST':
        form = BloggerEditForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return redirect("Login")
    else:
        form = BloggerEditForm()       
    return render(request,"AppBlogger/register.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect("Login")

def aboutme(request):
    return render(request, "AppBlogger/aboutme.html")

@login_required
def mensajeria(request):
    messages = Message.objects.all
    if request.method == "POST":
        formmsg = FormularioMessage(request.POST)
        print(formmsg)
        if formmsg.is_valid:
            info = formmsg.cleaned_data
            msg = Message(username=request.user, message=info['message'])
            msg.save()
            return redirect("Messages")
    else:
        formmsg = FormularioMessage()
    return render(request, "AppBlogger/mensajeria.html", {"form":formmsg, "Message":messages})

@login_required
def read_profile(request):
    profile = User.objects.all()
    contexto = {"Usuarios":profile}
    return render(request, 'AppBlogger/profile.html', contexto)

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, instance=request.user)
        if miFormulario.is_valid():
            if miFormulario.cleaned_data.get('imagen'):
                usuario.avatar.imagen = miFormulario.cleaned_data.get('imagen')
                usuario.avatar.save()
            miFormulario.save()
            return render(request, "AppBlogger/profile.html")
    else:
        miFormulario = UserEditForm()
    return render(request, "AppBlogger/editProfile.html", {"miFormulario":miFormulario, "usuario":usuario})

@login_required
def newBlog(request):
    if request.method == "POST":
        blogForm = FormularioBlog(request.POST)
        print(blogForm)
        if blogForm.is_valid:
            informacion = blogForm.cleaned_data
            blog = Blog(
                titulo = informacion['titulo'], 
                subtitulo = informacion['subtitulo'],
                autor = request.user,
                fecha = informacion['fecha'],
                imagen = informacion['imagen']
            )
            blog.save()
            return redirect("Pages")
    else:
        blogForm = FormularioBlog()
    return render(request, "AppBlogger/newBlog.html", {"blogForm":blogForm})

def nopage(request):
    return render(request, "AppBlogger/nopage.html")

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'AppBlogger/cambiarPass.html'
    success_url = reverse_lazy('Profile')

def deleteBlog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blog.delete()
    return redirect("Pages")

def updateBlog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == "POST":
        blogform = FormularioBlog(request.POST)
        print(blogform)
        if blogform.is_valid: 
            info = blogform.cleaned_data
            blog.titulo = info['titulo']
            blog.subtitulo = info['subtitulo']
            blog.cuerpo = info['cuerpo']
            blog.fecha = info['fecha']
            blog.imagen = info['imagen']
            blog.save()
            return redirect("Pages")
    else:
        blogform = FormularioBlog(
            initial={
                "titulo":blog.titulo,
                "subtitulo":blog.subtitulo,
                "cuerpo":blog.cuerpo,
                "fecha":blog.fecha,
                "imagen":blog.imagen
            }
        )
    return render(request, "AppBlogger/newBlog.html", {"blogForm":blogform})