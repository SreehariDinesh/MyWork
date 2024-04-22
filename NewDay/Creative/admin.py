from django.contrib import admin

# Register your models here.
from . models import(Register,Gallery)

admin.site.register(Register)
admin.site.register(Gallery)