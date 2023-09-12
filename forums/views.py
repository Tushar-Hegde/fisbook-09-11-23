from django.shortcuts import render
from .models import Forum,Events,Notices
from django.utils import timezone
from django.db.models import Q
# Create your views here.

def forum(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    events = Events.objects.filter(forum__id = forum_id).order_by('date').filter(Q(date__gte=timezone.now()))
    notices = Notices.objects.filter(forum__id=forum_id)
    context = {'forum':forum,'events':events,'notices':notices,}
    return render(request,'forum.html',context)

def event(request,event_id):
    event = Events.objects.get(id=event_id)
    context = {'event':event,'forum':forum}
    return render(request,'event.html',context)

def member_list(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    user_forums = request.user.forums.all()
    if forum.is_public or forum in user_forums:
        members = forum.users.all()
        mods = forum.mods.all()
        context = {'members':members,'mods':mods}
        return render(request,'members.html',context)
    else:
        valid = False
        context = {'valid':valid}
        return render(request,'invalid.html',context)
