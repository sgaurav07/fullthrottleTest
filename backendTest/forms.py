from django import forms 
from django.contrib.admin.widgets import AdminDateWidget
# import GeeksModel from models.py 
from .models import *
from django.forms.fields import DateField

class UserForm(forms.ModelForm): 
    # specify the name of model to use 
    class Meta: 
        model = User 
        fields = "__all__"

class ActivityPeriod(forms.ModelForm):

    class Meta:
        model = Activity_Period
        fields = ["start_time","end_time","user"]