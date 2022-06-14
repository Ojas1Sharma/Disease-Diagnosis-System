from django.contrib import admin
from .models import Heart, Kidney,Liver

# Register your models here.
admin.site.register(Heart)
admin.site.register(Kidney)
admin.site.register(Liver)