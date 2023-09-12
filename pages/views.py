from django.shortcuts import render, redirect
from django.urls import reverse 
from django.utils import timezone
from forums.models import Forum,Events
from datetime import datetime
from django.db.models import Q
from django.contrib.auth import get_user_model
# Create your views here.
CustomUser = get_user_model()

def home(request):
    if request.user.is_authenticated:
        forums = request.user.forums.all()
        users_events = request.user.events_added.all().order_by('date').filter(Q(date__gte=timezone.now()))
        events = Events.objects.filter(forum__in=forums).order_by('date').filter(Q(date__gte=timezone.now()))
        context={'forums':forums,'users_events':users_events,'events':events,}
        return render(request,'home.html',context)
    else:
        return redirect(reverse('users:login'))
    
    
def explore(request):
    forums = Forum.objects.filter(is_public=True)
    events = Events.objects.filter(is_public=True).order_by('date').filter(Q(date__gte=timezone.now()))
    context = {'forums':forums,'events':events}
    return render(request,'explore.html',context)
    

def user(request,reg_no):
    user = CustomUser.objects.get(reg_no=reg_no)
    context = {'reg_no':reg_no,'user':user,}
    return render(request,'user.html',context)
    