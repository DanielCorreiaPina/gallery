from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from .forms import ImageForm

from .models import Image

def index(request):
    image_list = Image.objects.all()
    return render(request, 'gallery/index.html', {'image_list': image_list})

def details(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/details.html', {'image': image})

def upload(request):
    # Process images uploaded by users# 
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image_title_exists = Image.objects.filter(title=form.cleaned_data['title']).exists()
            if image_title_exists:
                error = 'There is an image with "' + form.cleaned_data['title'] + '" as title already, choose other title'
                return render(request, 'gallery/upload.html', {'form': form, 'error': error})
            else:
                form.save()
                # Get the current instance object to display in the template
                img_obj = form.instance
                return render(request, 'gallery/upload.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'gallery/upload.html', {'form': form})

def delete_item(request, image_id):
    image = Image.objects.get(pk=image_id).delete()
    image_list = Image.objects.all()
    return render(request, 'gallery/index.html', {'image_list': image_list})