from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('vinyls/', views.vinyls_index, name='index'),
  path('vinyls/<int:vinyl_id>/', views.vinyls_detail, name='detail'),
  path('vinyls/create/', views.VinylCreate.as_view(), name='vinyls_create'),
  path('vinyls/<int:pk>/update/', views.VinylUpdate.as_view(), name='vinyls_update'),
  path('vinyls/<int:pk>/delete/', views.VinylDelete.as_view(), name='vinyls_delete'),
  path('vinyls/<int:vinyl_id>/add_listening/', views.add_listening, name='add_listening'),
  path('vinyls/<int:vinyl_id>/add_cover/', views.add_cover, name='add_cover'),
  path('vinyls/<int:vinyl_id>/assoc_concert/<int:concert_id>/', views.assoc_concert, name='assoc_concert'),
  path('vinyls/<int:vinyl_id>/unassoc_concert/<int:concert_id>/', views.unassoc_concert, name='unassoc_concert'),
  path('concerts/', views.ConcertList.as_view(), name='concerts_index'),
  path('concerts/<int:pk>/', views.ConcertDetail.as_view(), name='concerts_detail'),
  path('concerts/create/', views.ConcertCreate.as_view(), name='concerts_create'),
  path('concerts/<int:pk>/update/', views.ConcertUpdate.as_view(), name='concerts_update'),
  path('concerts/<int:pk>/delete/', views.ConcertDelete.as_view(), name='concerts_delete'),
]