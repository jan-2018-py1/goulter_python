# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# the index function is called when root is visited
def index(request):
    context = {
        'all_friends' : User.objects.all()
    }
    
    return render(request,"srusers_app/index.html", context)

def new(request):
    return render(request,'srusers_app/adduser.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request,error, extra_tags=tag)
        return redirect('/users')
    else:
        u1 = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
        u1.save()
        user_data = u1.id
        user_path = '/users/'+str(user_data)
        return redirect(user_path)


# def create(request):
#     print "*********************IN CREATE"
#     u1 = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
#     u1.save()
#     user_data = u1.id
#     user_path = '/users/'+str(user_data)
#     print "*********************user_path " + user_path
#     return redirect(user_path)
    
def show(request,uid):
    if request.method == 'GET':
        context = {
            'id':uid,
            'user':User.objects.get(id=uid)
        }
        return render(request,"srusers_app/user_profile.html", context)
    else:
        request.session['id'] = uid
        request.session['first_name'] = request.POST['first_name']
        request.session['last_name'] = request.POST['last_name']
        request.session['email'] = request.POST['email']
        return redirect('/users/update')

def update(request):
    u1 = User.objects.get(id=request.session['id'] )
    u1.first_name = request.session['first_name']
    u1.last_name = request.session['last_name']
    u1.email = request.session['email']
    u1.save()
    user_path = '/users/'+str(request.session['id'])
    return redirect(user_path)
        

def edit(request,uid):
    print "*****************"
    print uid
    context = {
        'id':uid,
        'user':User.objects.get(id=uid)
    }
    
    return render(request,'srusers_app/edit_profile.html',context)

def destroy(request,uid):
    u = User.objects.get(id=uid)
    u.delete()
    return redirect('/users')