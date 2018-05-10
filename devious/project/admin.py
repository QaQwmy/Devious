from django.contrib import admin
from project.models import Project,Tag
# Register your models here.
admin.site.register([Project,Tag])