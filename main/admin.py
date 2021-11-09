from django.contrib import admin
from .models import Todo, ToMeet

# Register your models here.

admin.site.register(Todo)
admin.site.register(ToMeet)