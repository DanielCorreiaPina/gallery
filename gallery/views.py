from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Image

def index(request):
    image_list = Image.objects.all()
    context = {'image_list': image_list}
    return render(request, 'gallery/index.html', context)

def details(request, image_id):
    """ try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    return render(request, 'gallery/details.html', {'image': image}) """
    image = get_object_or_404(Image, pk=image_id)
    return render(request, 'gallery/details.html', {'image': image})

def upload(request):
    return HttpResponse("You're at upload page.")