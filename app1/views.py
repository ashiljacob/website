from datetime import date

from django.contrib.messages.storage import session
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from app1.models import User


# Home Page
from app1.serializers import userSerializer


def home(request):
    return render(request, 'index.html')


# User Dash Board
@csrf_exempt
def dash_board(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            global user
            user = User.objects.get(username=request.POST['username'], password=request.POST['password'])

            #request.session['user'] = user

            act = User.objects.get(id=user.id)
            act.login_time = datetime.now()
            act.save()
            return render(request, 'dash.html', {'user': user, })

        else:
            return render(request, 'index.html')


# Registration Page
@csrf_exempt
def registration(request):
    return render(request, 'reg.html')


# user Registration
@csrf_exempt
def reg_upload(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password1']:

            reg = User(name=request.POST['name'], username=request.POST['username']
                       , password=request.POST['password'])
            reg.save()
            return render(request, 'index.html')
        else:
            return HttpResponse("<script>alert('Password didnt match')</script>")
            return redirect('/')
    else:
        return HttpResponse("<h1>Error While Registering.. TRy Again..</h1>")





@csrf_exempt
def logout(request):
    if request.method == "POST":
        act = User.objects.get(id=user.id)
        act.logout_time=datetime.now()
        act.save()
        return render(request,'index.html')
    else:
        return HttpResponse("<h1>Error While LogOut..!!</h1>")


# REst
class userList(APIView):

    def get(self,request):
        user1 = User.objects.all()
        serializer = userSerializer(user1, many=True)
        return Response(serializer.data)
