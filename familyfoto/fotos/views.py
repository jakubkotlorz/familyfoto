from django.conf import settings
from django.shortcuts import render
from .models import Foto

def index(request):
    images = [f"{settings.MEDIA_URL}fotos/img-3.jpg",
            f"{settings.MEDIA_URL}fotos/img-2.jpg", 
            f"{settings.MEDIA_URL}fotos/img-1.jpg"]
    images = Foto.objects.all()
    context = {'images': images}
    return render(request, 'fotos/index.html', context)
