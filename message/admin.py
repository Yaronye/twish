from django.contrib import admin

# Register your models here.
from .models import Secret

admin.site.register(Secret)