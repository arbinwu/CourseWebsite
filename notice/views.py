from django.shortcuts import render
from notice.models import Notice
from django.contrib import auth


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
    result = Notice.objects.all()
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'result': result,
        }
    else:
        content = {
            'state': state,
            'result': result,
        }
    return render(request, 'notice.html', content)


def details(request):
    state = None
    # id = request.GET['id']
    notice = Notice.objects.get(id=request.GET['id'])
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'notice_title': notice.title,
            'notice_author': notice.author,
            'notice_time': notice.time,
            'notice.content': notice.content,
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
