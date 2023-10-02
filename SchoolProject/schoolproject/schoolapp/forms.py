from django import forms
from .models import Department,Course

class CategoryForm(forms.Form):
    department = forms.ChoiceField(choices=[('civil','Civil'),('mech','Mechanical'),('cs','Computer Science'),('elec','Electrical')])
    course = forms.ChoiceField(choices=[('','Select Course')],required=False)
