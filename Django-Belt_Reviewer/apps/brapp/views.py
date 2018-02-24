# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Book, Author, Review
import bcrypt

# the index function is called when root is visited
# -*- coding: utf-8 -*-

# the index function is called when root is visited

#1
def index(request):
  return render(request,"brapp/registrationForm.html")

def doregister(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        u1 = User(name = request.POST['name'], alias = request.POST['alias'], email = request.POST['email'], password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()))
        u1.save()
        # request.session['id']=u1.id
        # request.session['first_name']=u1.first_name
        return redirect('/registered')

def registered(request):
    return render(request, "brapp/registered.html")

def login(request):
    post_password = request.POST['password']
    post_email = request.POST["email"]
    print "*****************post_email " + post_email
    print "*****************post_pass " + post_password
    
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        try:
            u = User.objects.get(email = post_email)
            print "****************successful try"
            u.save()
            print u.id
            if bcrypt.checkpw(post_password.encode(), u.password.encode()):
                print "password match"
                request.session['id']=u.id
                print "*********** "
                print request.session['id']
                return redirect('/books')
            return redirect('/')
        except:
            return redirect('/')
    
def books(request):
    if 'id' in request.session:
        print "***************id is in session"
        u = User.objects.get(id = request.session['id'])
        user_name = u.name
        print "user name is " + user_name
        
        unique_reviews = []
        reviews = Review.objects.all()
        for review in reviews:
            if review.books not in unique_reviews:
                unique_reviews.append(review.books)

        context = {
            'user' : user_name,
            # 'reviews':Review.objects.all().distinct(),
            # 'reviews':Review.objects.all(),
            'reviews' : unique_reviews,
            # 'reviews':Review.objects.distinct(books.title),
            '3rev' : Review.objects.order_by('-created_at')[:3][::1]
        }
        return render(request, "brapp/dashboard.html", context) 
   

def getabook(request):
    return render(request, "brapp/booksadd.html")

def processbook(request): 
        b1 = Book(title = request.POST['title'])
        b1.save()
               
        # a1 = Author(name = request.POST['author'])
        if request.POST['author']!='':
            a1 = Author(name = request.POST['author'])
        else:
            a1 = Author(name = request.POST['authors'])

        a1.save()
        b1.author = a1
        b1.save()
        r1 = Review(description = request.POST['review'], stars = request.POST['stars'])
        r1.save()
        # r1.books.add(b1)
        b1.reviews.add(r1)
        u1 = User.objects.get(id=request.session['id'])
        u1.userreviews.add(r1)
        # b1.review = r1
        # b1.save()

    # booktitle = request.POST['name']
        bookurl = '/books/' +str(b1.id)
        return redirect (bookurl)

def processreview(request,bookid):
    b1 = Book.objects.get(id=bookid)
    b1.save()
    r1 = Review(description = request.POST['review'], stars = request.POST['stars'])
    r1.save()
    b1.reviews.add(r1)
    u1 = User.objects.get(id=request.session['id'])
    u1.save()
    u1.userreviews.add(r1)
    bookurl = '/books/' +str(bookid)
    return redirect (bookurl)



def bookwall(request,bookid):
    # print '*************bookid ' + bookid
    context = {
        'title':Book.objects.get(id=bookid).title,
        'bookid':bookid,
        'author':Book.objects.get(id=bookid).author,
        'review':Book.objects.get(id=bookid).reviews.all()
        # 'review':Book.objects.get(id=bookid).distinct('title')
        # ModelName.objects.distinct('fieldname')

    }
    return render(request, "brapp/bookinfo.html", context)

def users(request,uid):

    user_unique_reviews = []
    reviews = Review.objects.filter(users=uid)
    for review in reviews:
        if review.books not in user_unique_reviews:
            user_unique_reviews.append(review.books)
    context = {
        'u' : User.objects.get(id=uid),
        'total_reviews':Review.objects.filter(users=uid).count(),
        # 'review':Review.objects.filter(users=uid)
        #  'review':Review.objects.filter(users=uid)
         'reviews':user_unique_reviews
    }
    return render(request, "brapp/user.html", context)

def delete_review(request, rid, bookid):
    r = Review.objects.get(id=rid)
    r.delete()
    bookurl = '/books/' +str(bookid)
    return redirect(bookurl)


def logout(request):
  request.session.clear()
  return redirect("/")





