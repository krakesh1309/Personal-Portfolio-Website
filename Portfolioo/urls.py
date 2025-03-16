from django.contrib import admin
from django.urls import path
from Port import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL ("/")
    path('home/', views.home, name='home_page'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
