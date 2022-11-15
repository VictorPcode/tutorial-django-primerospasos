from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["firstname"]
        
    template = loader.get_template('landing.html')
    context = {
        'mymembers': mymembers,
    }
    
    return HttpResponse(template.render(context, request))

def add(request):
    template = loader.get_template('addmb.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Members(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))