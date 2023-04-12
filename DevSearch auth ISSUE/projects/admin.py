from django.contrib import admin

# Register your models here.
from .models import Project
from .models import Tag
from .models import Review

admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Review)
