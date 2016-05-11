from django.shortcuts import render
# from  django.contrib.auth.models import User
from django.contrib import auth
from notice.models import Notice


# Create your views here.
def index(request):
    state = None
    notice = Notice.objects.order_by('-time')[0]
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'notice_title': notice.title,
            'notice_content': notice.content,
            'notice_id': notice.id,
        }

    else:
        content = {
            'state': state,
            'notice_title': notice.title,
            'notice_content': notice.content,
            'notice_id': notice.id,
        }

    return render(request, 'index.html', content)


def login(request):
    notice = Notice.objects.order_by('-time')[0]
    if 'username' in request.POST:
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)

            # Redirect to a success page.
            state = 'login'
            content = {
                'state': state,
                'user': request.user.first_name,
            }
            # print(request.user.is_staff)
            return render(request, 'index.html', content)
        else:  # Show an error page
            state = None
            is_error = True
            content = {
                'state': state,
                'is_error': is_error,
                'notice_title': notice.title,
                'notice_content': notice.content,
                'notice_id': notice.id,
            }
            return render(request, 'login.html', content)

    else:
        return render(request, 'login.html')


def logout(request):
    notice = Notice.objects.order_by('-time')[0]
    if request.user.is_authenticated():
        auth.logout(request)
        state = None
        content = {
            'state': state,
            'notice_title': notice.title,
            'notice_content': notice.content,
            'notice_id': notice.id,
        }
        return render(request, 'index.html', content)

# def login(request):
#     # user = auth.authenticate(username='john', password='secret')
#     db = User.objects.get(username='9999')
#     print(db.name)
