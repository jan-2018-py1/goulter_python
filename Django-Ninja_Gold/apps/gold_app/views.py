# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
# the index function is called when root is visited
def index(request):
    #show the 4 forms
    if not 'yourGold' in request.session.keys():
        request.session['yourGold'] = 0
        request.session['currentWin'] = 0
        request.session['currentPlace'] = 'Glens House'
        request.session['history']=[]
        return render(request,"gold_app/index.html")
    else:
        return render(request,"gold_app/index.html")

def process_param(request,place):
    print "****************GOT PARAM" + place
    houseDict = {}
    request.session.modified = True
    if place == 'farm':
    #using the hidden input would be
    #if request.POST['building'] == 'farm':
      houseDict['currentPlace'] = 'farm'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(9, 21))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    elif place == 'cave':
      houseDict['currentPlace'] = 'cave'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(4, 11))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    elif place == 'house':
      houseDict['currentPlace'] = 'house'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(1, 6))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    else:
      houseDict['currentPlace'] = 'casino'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(-51, 51))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')  

def process(request):
    houseDict = {}
    request.session.modified = True
    if request.POST['building'] == 'farm':
      houseDict['currentPlace'] = 'farm'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(9, 21))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    elif request.POST['building'] == 'cave':
      houseDict['currentPlace'] = 'cave'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(4, 11))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    elif request.POST['building'] == 'house':
      houseDict['currentPlace'] = 'house'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(1, 6))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')
    else:
      houseDict['currentPlace'] = 'casino'
      houseDict['timeStamp'] = datetime.now().strftime("%Y/%m/%d %I:%m:%p")
      houseDict['currentWin'] = int(random.randrange(-51, 51))
      request.session['yourGold'] += houseDict['currentWin']
      request.session['history'].append(houseDict)
      return redirect('/')    
def reset(request):
   request.session.clear()
   return redirect('/')
