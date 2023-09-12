from django.utils import timezone
from calendar import HTMLCalendar
from .models import Events


class Calendar(HTMLCalendar):
    
    def __init__(self,year=None,month=None):
        self.year = year
        self.month = month
        super(Calendar,self).__init__()
    
    def formatday(self,day,events):
        events_per_day = events.filter(date__day = day)
        d = ''
        for event in events_per_day:
            d+= '''<li> <a href="{% url 'forums:event' event.id %}">'''+event.title+'''</a> </li>'''
        if day != 0:
            return f"<td><span class='date'>{day}"
            