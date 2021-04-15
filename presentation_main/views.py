from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.views import View
from django.http import HttpResponse
from .visual import result, Visualization

def index(request):
    return render(request, 'pages/index.html', {})

def image_list(request):
    return render(request, 'pages/list.html', {})

def upload_image(request):
    return render(request, 'pages/upload.html', {})

class FileUp(View):
    def post(self, request):
        video_file = request.FILES['file']
        default_storage.save(video_file.name, video_file)
        return redirect('../upload/#work')
