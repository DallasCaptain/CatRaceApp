from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.
def index(request):
    return render(request,'catApp/index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.validate(request.POST)
        if len(errors) < 1:

            pwhash = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt(10))
            name = request.POST['name']
            bday = request.POST['bday']
            user = User.objects.create(uname = name, bday = bday, password = pwhash.decode())
            # user = User()
            # user.name = name
            # user.bday = bday
            # user.password = pwhash.decode()
            # user.save()
            context = {
                'user':user,
            }
            request.session['name']=user.uname
            return redirect('/success')
        for error in errors:
            messages.error(request,error)
    return redirect('/')

def login(request):
    if request.method=="POST":
        user = User.objects.get(uname=request.POST['name'])
        if bcrypt.checkpw(request.POST['password'].encode(),user.password.encode()):
            request.session['name'] = user.uname
            return redirect('/success')
        messages.error(request,'bad password')
        return redirect('/')
    return redirect('/')
        

def success(request):
    if 'name' in request.session:
        user = User.objects.get(uname = request.session['name'])
        context = {
            'user' : user,
            'cats' : Cat.objects.all(),
            'races': CatRace.objects.all(),
        }
        return render(request,'catApp/cats.html',context)
    messages.error(request, 'LOGIN OR ELSE!')
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def addCat(request):
    if request.method=='POST':
        user = User.objects.get(uname=request.session['name'])
        cat = Cat.objects.create(name=request.POST['name'],owner=user)
        return redirect('/success')
    messages.error(request,'NO CHEATING!')
    return redirect('/success')
    
def removeCat(request):
    if request.method=='POST':
        
        user = User.objects.get(uname=request.session['name'])
        
        cat = Cat.objects.get(name=request.POST['name'])

        if cat.owner != user:
            messages.error(request,'NO Killing others cats!')
            return redirect('/success')
        cat.delete()
        return redirect('/success')
    messages.error(request,'NO CHEATING!')
    return redirect('/success')


def addRace(request):
    catRace = CatRace(name=request.POST['name'])
    catRace.save()
    print(request.POST.items())
    if 'cat1' in request.POST:
        catRace.racers.add(request.POST['cat1'])
    if 'cat2' in request.POST:
        catRace.racers.add(request.POST['cat2'])
    if 'cat3' in request.POST:
        catRace.racers.add(request.POST['cat3'])
    if 'cat4' in request.POST:
        catRace.racers.add(request.POST['cat4'])
    catRace.save()
    return redirect('/success')