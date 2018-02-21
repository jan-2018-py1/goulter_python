# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
# the index function is called when root is visited
def index(request):
    context={
        'all_courses':Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error, extra_tags=tag)
        return redirect('/')
    else:
        c1 = Course(name = request.POST['name'], description = request.POST['description'])
        c1.save()
        return redirect('/')
    # c1 = Course(name = request.POST['name'], description = request.POST['description'])
    # c1.save()
    # return redirect('/')

def destroy_check(request,uid):
    if request.method == 'GET':
        context={
            'course':Course.objects.get(id=uid)
        }
        return render(request, 'courses_app/destroy.html', context)
   

def dodestroy(request,uid):
    if request.POST['decision'] == 'Yes':
        c = Course.objects.get(id=uid)
        c.delete()
        return redirect('/')
    else:
        return redirect('/') 
