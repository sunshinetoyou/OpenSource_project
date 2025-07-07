from django.contrib import admin
from .models import Project, Vote

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('subject', 'avg_score', 'detail')  # avg_score 필드 추가

admin.site.register(Project, ProjectAdmin)
admin.site.register(Vote)