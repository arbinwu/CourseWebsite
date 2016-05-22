from django.shortcuts import render
# from django.http import HttpResponse
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    is_error = False
    error = ''
    if 'username' in request.POST:
        username = str(request.POST['username'])
        first_name = str(request.POST['name'])
        password = str(request.POST['password'])
        repeat_password = str(request.POST['repeat_password'])
        # print(username)
        if username == '':
            is_error = True
            error = '用户名不能为空'
        elif not username.isalnum():
            is_error = True
            error = '用户名必须为数字或字符'
        elif User.objects.filter(username=username):
            is_error = True
            error = '用户名已存在'
        elif password == '' or repeat_password == '':
            is_error = True
            error = '密码不能为空'
        elif password != repeat_password:
            is_error = True
            error = '两次输入的密码不一致'
        elif first_name == '':
            is_error = True
            error = '姓名不能为空'
        if not is_error:
            error = '注册成功'
            new_user = User.objects.create_user(username=username,
                                                password=password,
                                                first_name=first_name)
            new_user.save()
    else:
        pass
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'is_error': is_error,
            'error': error,
            'state': state,
            'user': request.user.first_name,
        }
    else:
        state = None
        content = {
            'is_error': is_error,
            'error': error,
            'state': state,
        }
    return render(request, 'register.html', content)


def test(request):
    return render(request, 'test.html')
