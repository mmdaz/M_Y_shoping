from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    # if request.method == 'POST':
    #     user_name = request.POST['user_name']
    #     password = request.POST['password']
    #     User.objects.create(username=user_name, password=password)
    return render(request, template_name="authorization/registeration.html")


def login(request):
    return render(request, 'authorization/login.html')

@csrf_exempt
def add(request):
    if request.method == 'POST':
        myDict = dict(request.POST)
        information = myDict['name']
        print(information)
        print(myDict)
        user_name = information[0]
        password = information[1]
        User.objects.create(username=user_name, password=password)
        return HttpResponse("<h1>User added!</h1>")

