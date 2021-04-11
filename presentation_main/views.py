from django.http import HttpResponse
from .forms import UploadForm
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'pages/index.html', {})

def image_list(request):
    return render(request, 'pages/list.html', {})

def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = UploadForm()
    return render(request, 'pages/upload.html', {'form':form})


