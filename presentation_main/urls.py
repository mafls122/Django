from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from presentation_main.views import FileUp

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_file/', FileUp.as_view()),
    path('upload/', views.upload_image, name='upload_image'),
    path('list/', views.image_list, name='image_list'),
]
