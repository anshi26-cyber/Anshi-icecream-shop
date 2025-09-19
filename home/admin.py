from django.contrib import admin
from home.models import Contact
from .models import IceCream

# Register your models here.
admin.site.register(Contact)
admin.site.register(IceCream)