from django.shortcuts import render 
from .models import *
import jsonify
from .forms import UserForm, ActivityPeriod
from django.http import HttpResponse
import json
from datetime import datetime

#API to add new members
def home_view(request): 
    
    user_form = UserForm(request.POST or None) 
    activity_form = ActivityPeriod()
    
    if user_form.is_valid(): 
        user_form.save()
        url = '/activity'
        return render(request,"activity.html",{'activity_form':activity_form, 'url':url})
    return render(request,"home.html", {'user_form':user_form})

#API to add activity period of members
def activity_view(request):
    activity_form = ActivityPeriod(request.POST or None)
    if activity_form.is_valid():
        activity_form.save()
    return render(request,"activity.html", {'activity_form':activity_form})

#API to view the data in json format

def dataretrive(request):
    userDetails = User.objects.all()
    members = []
    retval = dict()
    retval["ok"] = True
    for user in userDetails:
        details = dict()
        details["id"] = user.id
        details["real_name"] = user.real_name
        details["tz"] = user.tz
        activityObj = Activity_Period.objects.filter(user = str(user.id))
        activity_periods = []
        for a in activityObj:
            activity = dict()
            s = a.start_time
            e = a.end_time
            activity["start_time"] = s.strftime("%d %b, %Y %H:%M%p")
            activity["end_time"] = e.strftime("%d %b, %Y %H:%M%p")
            activity_periods.append(activity)
        activityObj=None
        details["activity_periods"] = activity_periods
        members.append(details)
    retval['members'] = members
    
    return HttpResponse(json.dumps(retval), content_type="application/json")
