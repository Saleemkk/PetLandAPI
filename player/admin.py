from django.contrib import admin
from .models import Land, Pet, Player


admin.site.register(Player)

admin.site.register(Pet)

admin.site.register(Land)