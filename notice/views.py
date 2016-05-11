from django.shortcuts import render
from notice.models import Notice
from django.contrib import auth
from django.http import HttpResponseRedirect

# 动态建表
# def create(request):
# cursor = connection.cursor()
# Create table as per requirement
# name = 'notice'
# str = 'CREATE TABLE ' + name
# sql = str + '( FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT)'
# cursor.execute(sql)
# no = Notice.objects.create(title='test', author='arbin',content='111')
# no.save()

# 查询不在models中的表
# cur = connection.cursor()
# cur.execute('select * from notice')
# result = cur.fetchone()
# print(result)
# return render(request, 'test.html')

# Create your views here.
# def create(request):
#     # cursor = connection.cursor()
#     # # Create table as per requirement
#     # str = 'notice'
#     # sql = """CREATE TABLE old (
#     #          FIRST_NAME  CHAR(20) NOT NULL,
#     #          LAST_NAME  CHAR(20),
#     #          AGE INT,
#     #          SEX CHAR(1),
#     #         )
#     #         ALTER TABLE;
#     #         """
#     # cursor.execute(sql)
#
#
#     return render(request, 'test.html')


# from Django.db import models


# class Secretcode(models.Model):
#     timestamp = models.DateTimeField(autonow=True)
#     uid = models.CharField(max_length=32, )
#     secretcode = models.CharField(max_length=10)
#     cid = models.CharField(max_length=20, blank=True, null=True)

def view_notice(request):
    state = None
    result = Notice.objects.order_by('-time')
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'result': result,
            'publish': request.user.is_staff,
        }
    else:
        content = {
            'state': state,
            'result': result,
        }
    return render(request, 'notice.html', content)


def details(request):
    state = None
    notice = Notice.objects.get(id=request.GET['id'])
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'notice_title': notice.title,
            'notice_author': notice.author,
            'notice_time': notice.time,
            'notice_content': notice.content,
        }
    else:
        content = {
            'state': state,
            'notice_title': notice.title,
            'notice_author': notice.author,
            'notice_time': notice.time,
            'notice_content': notice.content,
        }
    return render(request, 'details.html', content)


def add(request):
    state = None
    is_error = False
    error = ''
    new_title = str(request.POST['new_title'])
    new_content = str(request.POST['new_content'])
    if new_title == '':
        is_error = True
        error = '公告标题不能为空'
    elif new_content == '':
        is_error = True
        error = '公告内容不能为空'
    else:
        new_author = request.user.first_name
        new_notice = Notice.objects.create(title=new_title, author=new_author, content=new_content)
        new_notice.save()
        error = '公告发布成功，请查看！'
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'is_error': is_error,
            'error': error,
            'user': request.user.first_name,
        }
    else:
        content = {
            'state': state,
            'is_error': is_error,
            'error': error,
        }
    return HttpResponseRedirect('notice.html')
