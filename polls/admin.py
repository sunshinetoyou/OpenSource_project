from django.contrib import admin
from .models import Project, Vote

admin.site.register(Project)
admin.site.register(Vote)