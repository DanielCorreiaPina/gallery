from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ImageForm

from .models import Image

def index(request):
    image_list = Image.objects.all()
    context = {'image_list': image_list}
    return render(request, 'gallery/index.html', context)

def details(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/details.html', {'image': image})

def upload(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'gallery/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})