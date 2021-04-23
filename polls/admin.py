from django.contrib import admin

from .models import Planning
from .models import Student
from .models import Secretary
from .models import Instructor

# Register your models here.
admin.site.register(Planning)
admin.site.register(Student)
admin.site.register(Secretary)
admin.site.register(Instructor)
