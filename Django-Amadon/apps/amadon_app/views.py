# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    return render (request, "amadon_app/buy.html")

def buy(request):
    if 'count' in request.session:
        request.session['count']+=1
    else:
        request.session['count'] = 1
    request.session['quantity'] = request.POST['choice']
    request.session['price'] = int(request.POST['price']) * int(request.session['quantity'])    
    print "********************quantity" + str(int(request.session['quantity']))
    print "********************price" + str(int(request.session['price']))
    if 'grandtotal' in request.session:
        request.session['grandtotal']+=int(request.session['price'])
        print "*************GT HERE" + str(request.session['grandtotal'])
    else:
        print "*************NOT GT YET"
        request.session['grandtotal'] = 0
        request.session['grandtotal'] = int(request.session['price'])
    return redirect ("/amadon/checkout")

def checkout(request):
    return render (request,"amadon_app/thank_you.html")

def clear(request):
    request.session.clear()
    return redirect('/amadon')   
