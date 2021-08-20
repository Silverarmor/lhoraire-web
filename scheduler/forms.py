from django import forms
from django.forms import ModelForm, fields
from django.forms.models import modelformset_factory
from django.forms.widgets import TextInput
from .models import TaskInfo, UserInfo
from django.forms import formset_factory

from datetime import date


class DateInput(forms.DateInput):
    input_type = 'date'
    attrs = {"min": date.today().strftime("%Y-%m-%d")}


TaskModelFormSet = modelformset_factory(
    TaskInfo, exclude=('user',))


class TaskForm(ModelForm):
    # due_date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateInput(
    #         attrs={
    #             'type': 'date',
    #             'class': 'date-selector',
    #             'id': 'datepicker'
    #         },
    #     ),
    # )

    class Meta:
        model = TaskInfo
        exclude = ['user', 'modified_date', 'start_date', 'days_needed']
        widgets = {
            'due_date': TextInput(attrs={"id": "datepicker", "required": "True"}),
            'color': TextInput(attrs={"type": "color", "class": "form-control form-control-color"}),
            'task_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Study Physics', "required": "True"}),
            'task_description': forms.Textarea(attrs={'class': 'form-control', 'rows': '2', "required": "True"}),
            'gradient': forms.Select(attrs={'class': 'form-select'}),
            'hours_needed': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'required': 'True', 'step': 0.5}),
            'days_needed': forms.TextInput(attrs={'class': 'form-control'})
        }


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['user']
        widgets = {
            'time_zone': forms.Select(attrs={'class': 'form-select', 'id': 'time_zone_select'}),
            'week_day_work': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'})
        }

    # task_name = forms.CharField(label='Task Name', max_length=100)
    # work = forms.IntegerField(label='Hours')
    # due_date = forms.CharField(label='Due Date', max_length=20)
    # gradient = forms.CharField(label='Gradient', max_length=1, initial='+')
