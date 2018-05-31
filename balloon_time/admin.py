from django.contrib import admin

# Register your models here.

from .models import Party, Clown
admin.site.register([Party, Clown])
