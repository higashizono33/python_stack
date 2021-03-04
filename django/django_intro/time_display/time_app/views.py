from django.shortcuts import render, HttpResponse
from time import gmtime, strftime, localtime
# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "time2": strftime("%a, %d %b %Y %I:%M %p %Z", gmtime()),
        "time3": strftime("%d-%m-%Y %H:%M %p %x", gmtime()),
        "time4": strftime("%Y-%B-%d %A %H:%M:%S", gmtime()),
    }
    return render(request,'index.html', context)