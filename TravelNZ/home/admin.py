from django.contrib import admin

from .models import Agent, Duration, Tour

# Register your models here.
admin.site.register([Agent, Duration, Tour])