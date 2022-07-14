from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import BadHeaderError
from django.template import loader

# Create your views here.
User = get_user_model()

def register(request):
    next = request.GET.get('next', '/')
    try:
        username = request.POST['username']
        password = request.POST['password']
        auth_user = authenticate(request, username=username, password=password)
        try:
            login(request, auth_user)
            return HttpResponseRedirect(next)
        except:
            messages.error(request, 'Invalid credentials')
            return HttpResponseRedirect(next)
    except (KeyError):
        messages.error(request, 'Invalid credentials')



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']

        print("----------------- register called")
        print(username)
        print([password])
        print(firstname)
        print(lastname)
        print(email)

        messages.success(request, 
                        f'your accoun has been created! You can now log in.')
        return redirect('login')
    else:
        return render(request, 'users/register.html')