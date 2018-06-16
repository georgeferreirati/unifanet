from django.contrib import admin
from .models import Profile, Estudante, Professor, Coodenador

# Register your models here.
admin.site.register(Profile)
admin.site.register(Estudante)
admin.site.register(Professor)
admin.site.register(Coodenador)