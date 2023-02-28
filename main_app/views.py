from django.shortcuts import render

vinyls = [
  {'name': 'The Velvet Underground & Nico', 'artist': 'The Velvet Underground and Nico', 'released': 'March 12, 1967', 'label': 'Verve Records'},
  {'name': 'Abbey Road', 'artist': 'The Beatles', 'released': 'September 26, 1969', 'label': 'Apple Records'},
]


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def vinyls_index(request):
  return render(request, 'vinyls/index.html', {
    'vinyls': vinyls
  })