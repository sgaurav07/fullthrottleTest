from django import forms 
from django.contrib.admin.widgets import AdminDateWidget
# import GeeksModel from models.py 
from .models import *
from django.forms.fields import DateField

# Member add form
class UserForm(forms.ModelForm): 
    class Meta: 
        model = User 
        fields = "__all__"

# Activity Period add forms
class ActivityPeriod(forms.ModelForm):

    class Meta:
        model = Activity_Period
        fields = ["start_time","end_time","user"]