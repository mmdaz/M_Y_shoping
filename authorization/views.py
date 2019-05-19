from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from authorization.models import MyUser
from authorization.utils import email_is_valid


@csrf_exempt
def register(request):
    return render(request, template_name="authorization/registeration.html")


def login(request):
    if request.method == 'POST':
        input_dict = dict(request.POST)
        information = input_dict['name']
        user_name = information[0]
        password = information[1]
    return render(request, 'authorization/login.html')


@csrf_exempt
def add_user_to_db(request):
    if request.method == 'POST':
        input_dict = dict(request.POST)
        information = input_dict['name']
        user_name = information[0]
        password = information[1]
        email = information[2]
        if email_is_valid(email=email):
            messages.info(request=request, message="You are registered successfully.")
            MyUser.objects.create(username=user_name, password=password, email=email)
            # FIXME render a good html response .
            # return render(request=request, template_name='authorization/login.html')
            return render(request, '../templates/pages/index.html')
        else:
            return HttpResponse('<h1>We have an error</h1>')
