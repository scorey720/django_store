from django.urls import path
from mainapp import views


urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
]
