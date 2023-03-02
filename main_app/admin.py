from django.contrib import admin
from .models import Vinyl, Listening, Concert, Cover

admin.site.register(Vinyl)
admin.site.register(Listening)
admin.site.register(Concert)
admin.site.register(Cover)