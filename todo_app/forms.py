from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Task
        fields = ['name', 'importance', 'deadline', 'description']
        widgets = {
            "deadline": DatePickerInput(options={"format": "MM/DD/YYYY"}),
        }