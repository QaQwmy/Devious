from django.contrib import admin
from project.models import Project,Tag,Company
# Register your models here.
admin.site.register([Project,Tag,Company])