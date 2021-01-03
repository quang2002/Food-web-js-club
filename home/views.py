from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def info(request):
    return render(request, 'info.html')

def view_post(request, id):
    return render(request, 'post-view.html', {
        'post': models.post.objects.get(id=id)
    })
