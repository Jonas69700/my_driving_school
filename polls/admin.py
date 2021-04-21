from django.contrib import admin

from .models import Planning
from .models import Student

# Register your models here.
admin.site.register(Planning)
admin.site.register(Student)