from django.contrib import admin

from .models import Planning
from .models import Student
from .models import Secretary
from .models import Instructor

# from forms import PlanningForm

# class PlanningAdmin(admin.ModelAdmin):
#   list_display = ["location", "date_rdv", "hour", "created", "updated"]
#   form = PlanningForm
#   list_filter = ["location", "date_rdv"]
#   search_fields = ["location", "date_rdv"]

# Register your models here.
admin.site.register(Planning)
# , PlanningAdmin)
admin.site.register(Student)
admin.site.register(Secretary)
admin.site.register(Instructor)
