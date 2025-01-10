from django import forms
from .models import Resume


from django import forms

class ResumeForm(forms.Form):
    resume = forms.FileField()