# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from  django.utils.crypto  import get_random_string
# the index function is called when root is visited

def index(request):
    # attach key value pair
    context = {
    "word": get_random_string(length=14), 
    }
    if request.method == "POST": #when a user clicks submit
        if 'counter' in request.session.keys(): 
            request.session['counter']+=1
            return render(request, 'random_word/randomword.html', context)
        else: #when a user refershes the page
            request.session['counter']=0
            return render(request, 'random_word/randomword.html', context)
    else:
        if 'counter' in request.session.keys():
            request.session['counter']+=1
            return render(request, 'random_word/randomword.html', context)
        else:
            request.session['counter']=0
            return render(request, 'random_word/randomword.html', context)

def reset(request):
    if request.method == "POST": #when a user clicks reset
        request.session['counter']=0
        return redirect('/randomword/')
    else:
        request.session['counter']=0#when a user refershes the page
        return redirect('/randomword/')

