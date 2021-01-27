from django.shortcuts import render
from time import gmtime, strftime, localtime
import datetime
import pytz

def index(request):
    dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
    value2 = dt_utcnow.astimezone(pytz.timezone('US/Pacific'))

    context = {
        "time": value2.strftime("%I:%M %p"),
        "date": value2.strftime("%B %d, %Y"),
    }
    return render(request,'index.html',context)
