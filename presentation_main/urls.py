from django.urls import path
from presentation_main import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    ]