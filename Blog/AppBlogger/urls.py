from django.urls import path
from AppBlogger import views

urlpatterns = [
    path('', views.view_app, name="Pages"),
    path('accounts/login/', views.login_request, name="Login"),
    path('accounts/signup/', views.register_request, name="Signup"),
    path('accounts/profile/', views.read_profile, name="Profile"),
    path('messages/', views.mensajeria, name="Messages"),
    path('newblog/', views.newBlog, name="NewBlog"),
    path('editprofile/', views.editProfile, name="EditProfile"),
    path('about/', views.aboutme, name="Aboutme"),
    path('logout/', views.logout_request, name="Logout"),
    path('cambiarContrasenia/', views.PasswordChange.as_view(), name="CambiarContrasenia"),
    path('nopage/', views.nopage, name="Nopage"),
    path('deleteblog/<blog_id>', views.deleteBlog, name="DeleteBlog"),
    path('updateblog/<blog_id>', views.updateBlog, name="UpdateBlog"),
]