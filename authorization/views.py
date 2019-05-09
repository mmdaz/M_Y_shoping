from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        User.objects.create(username=user_name, password=password)
