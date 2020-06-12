from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from app1.models import User,Activity
from app1.serializers import UserSerializer,ActivitySerializer


def home(request):
    return render(request, 'index.html')


# User Dash Board
@csrf_exempt
def dash_board(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            user = User.objects.get(username=request.POST['username'], password=request.POST['password'])
            request.session['user'] = user.name

            Activity.objects.create(user=user,log_in=datetime.now())
            # Getting Id of the Actibvity Table
            temp = list(Activity.objects.filter(user=user))

            request.session['id'] = temp[-1].id # Passing Id of Activity to Signout

            # Getting User activity
            act = Activity.objects.filter(user=user)
            print("--------------------",act)
            return render(request, 'dash.html', {'user': user, 'act' :act})

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
        act = Activity.objects.get(id=request.session['id'])
        act.log_out = datetime.now()
        act.save()
        return render(request,'index.html')
    else:
        return HttpResponse("<h1>Error While LogOut..!!</h1>")


# REstFul API

class ActivityListView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = "activity-list"
