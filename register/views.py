from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name
        }
        return render(request, 'register.html', content)
    else:
        return HttpResponse('wu')
