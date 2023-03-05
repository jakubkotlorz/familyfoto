from django.conf import settings
from django.shortcuts import render
from .forms import FotoAddForm
from .models import Foto

def index(request):
    images = [f"{settings.MEDIA_URL}fotos/img-3.jpg",
            f"{settings.MEDIA_URL}fotos/img-2.jpg", 
            f"{settings.MEDIA_URL}fotos/img-1.jpg"]
    images = Foto.objects.all()
    context = {'images': images}
    return render(request, 'fotos/index.html', context)

def add_foto(request):
    foto_added = False
    if request.method == 'POST':
        form = FotoAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            foto_added = True
        else:
            print(form.cleaned_data)
    else:
        form = FotoAddForm()
    context = {'form': form, 'foto_added': foto_added}
    return render(request, 'fotos/add.html', context)
