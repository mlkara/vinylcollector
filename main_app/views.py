from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Vinyl
from .forms import ListeningForm


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
    listening_form = ListeningForm()
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl, 'listening_form': listening_form
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


def add_listening(request, vinyl_id):
    form = ListeningForm(request.POST)
    if form.is_valid():
        new_listening = form.save(commit=False)
        new_listening.vinyl_id = vinyl_id
    new_listening.save()
    return redirect('detail', vinyl_id=vinyl_id)
