from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect
from  django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def index(request):
    state = None
    content = {
        'state': state
    }
    return render(request, 'index.html', content)


def login(request):
    if 'username' in request.POST:
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        user = auth.authenticate(username=username, password=password)
        # print(name.name)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)

            # Redirect to a success page.
            state = 'login'
            content = {
                'state': state,
                'user': request.user.first_name,
            }
            return render(request, 'index.html', content)
        else:
            # Show an error page
            state = None
            content = {
                'state': state
            }
            return render(request, 'login.html', content)
    else:
        return render(request, 'login.html')

# def login(request):
#     # user = auth.authenticate(username='john', password='secret')
#     db = User.objects.get(username='9999')
#     print(db.name)
