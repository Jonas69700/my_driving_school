from django.http import HttpResponse
# from forms import PlanningForm
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're the polls index.")
