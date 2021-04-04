from django.contrib import admin
from .models import Semester, Subject, Chapter, Resource, Banner

# Register your models here.
admin.site.register(Semester)
admin.site.register(Subject)
admin.site.register(Chapter)
admin.site.register(Resource)
admin.site.register(Banner)
