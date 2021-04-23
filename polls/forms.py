from django import forms
from models import Planning

class PlanningForm(forms.ModelForm):
  class Meta:
    model = Planning
    fields = ['heure', 'date_rdv', 'lieu']
