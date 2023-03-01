from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def vinyls_index(request):
    vinyls = Vinyl.objects.all()
    return render(request, 'vinyls/index.html', {
        'vinyls': vinyls
    })


def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl
    })


class VinylCreate(CreateView):
    model = Vinyl
    fields = '__all__'

class VinylUpdate(UpdateView):
        model = Vinyl
        fields = ['artist', 'released', 'label']


class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls'
