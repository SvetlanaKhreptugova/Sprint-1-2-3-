from django.contrib import admin
from .models import User, Coord, Level, Image, Pass

admin.site.register(User)
admin.site.register(Coord)
admin.site.register(Level)
admin.site.register(Image)
admin.site.register(Pass)
