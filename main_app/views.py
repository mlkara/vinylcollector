from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Vinyl, Concert, Cover
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
    id_list = vinyl.concerts.all().values_list('id')

    concerts_vinyl_doesnt_have = Concert.objects.exclude(id__in=id_list)
    listening_form = ListeningForm()
    return render(request, 'vinyls/detail.html', {
        'vinyl': vinyl, 'listening_form': listening_form,
        'concerts': concerts_vinyl_doesnt_have
    })


class VinylCreate(CreateView):
    model = Vinyl
    fields = ['name', 'artist', 'released', 'label']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


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


class ConcertList(ListView):
    model = Concert


class ConcertDetail(DetailView):
    model = Concert


class ConcertCreate(CreateView):
    model = Concert
    fields = '__all__'


class ConcertUpdate(UpdateView):
    model = Concert
    fields = ['venue', 'city']


class ConcertDelete(DeleteView):
    model = Concert
    success_url = '/concerts'


def assoc_concert(request, vinyl_id, concert_id):
    Vinyl.objects.get(id=vinyl_id).concerts.add(concert_id)
    return redirect('detail', vinyl_id=vinyl_id)


def unassoc_concert(request, vinyl_id, concert_id):
    Vinyl.objects.get(id=vinyl_id).concerts.remove(concert_id)
    return redirect('detail', vinyl_id=vinyl_id)



def add_cover(request, vinyl_id):
    cover_file = request.FILES.get('cover-file', None)
    if cover_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            cover_file.name[cover_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(cover_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Cover.objects.create(url=url, vinyl_id=vinyl_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', vinyl_id=vinyl_id)
