from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from homework.models import *
import numpy as np


# Create your views here.
def view(request):
    state = None
    homework = Homework.objects.order_by('-time')
    if request.user.is_authenticated():
        state = 'login'
        content = {
            'state': state,
            'user': request.user.first_name,
            'homework': homework,
            'publish': request.user.is_staff,
        }
    else:
        content = {
            'state': state,
            'homework': homework,
        }
    return render(request, 'homeworklist.html', content)


def add_homework(request):
    author = request.user.first_name
    title = str(request.POST['new_title'])
    content = str(request.POST['new_content'])
    new_work = Homework.objects.create(author=author, title=title, content=content)
    new_work.save()
    return HttpResponseRedirect('homeworklist.html')


def homework_details(request):
    state = None
    homework = Homework.objects.get(id=request.GET['id'])
    if request.user.is_authenticated():
        state = 'login'
        results = Submit.objects.filter(homework_id=request.GET['id'])
        count = len(results)
        f = 0
        path = request.get_full_path()
        # print(path)
        if 'flag' in path:
            f = 1
        else:
            pass
        content = {
            'results': results,
            'count': count,
            'state': state,
            'user': request.user.first_name,
            'homework': homework,
            'permission': request.user.is_staff,
            'flag': f,
        }
    else:
        content = {
            'state': state,
            'homework': homework,
        }
    return render(request, 'homeworkdetails.html', content)


def upload(request):
    uploadfile = request.FILES['uploadfile']
    print(uploadfile)
    # print(uploadfile.name)
    # 信息存放到数据表
    u = Submit()
    u.homework_id = int(request.POST['homework_id'])
    u.author = request.user.first_name
    u.path = uploadfile
    u.save()
    return HttpResponseRedirect('homeworklist.html')


def score(request):
    obj_score = int(request.POST['score'])
    obj_id = int(request.POST['id'])
    obj = Submit.objects.filter(id=obj_id)[0]
    obj.score = obj_score
    obj.save()
    return HttpResponseRedirect('homeworkdetails.html?id=' + str(obj.homework_id))


class LevenshteinDistance:
    def leDistance(self, input_x, input_y):
        xlen = len(input_x) + 1  # 此处需要多开辟一个元素存储最后一轮的计算结果
        ylen = len(input_y) + 1

        dp = np.zeros(shape=(xlen, ylen), dtype=int)
        for i in range(0, xlen):
            dp[i][0] = i
        for j in range(0, ylen):
            dp[0][j] = j

        for i in range(1, xlen):
            for j in range(1, ylen):
                if input_x[i - 1] == input_y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[xlen - 1][ylen - 1]


def detection(request):
    homework_id = int(request.POST['homework_id'])
    ld = LevenshteinDistance()
    all_submit = Submit.objects.filter(homework_id=homework_id)
    # print(len(all_submit))
    source_name = [''] * len(all_submit)
    compare_name = [''] * len(all_submit)
    sim = [''] * len(all_submit)
    n = 0
    while n < len(all_submit):
        compare = 0
        source = all_submit[n]
        source_name[n] = source.author
        file1 = open(str(source.path)).read()
        file1.replace('#include', '')
        file1.replace('int', '')
        file1.replace('float', '')
        file1.replace('int main', '')
        file1.replace('using namespace std', '')
        file1.replace(';', '')
        file1.replace('(', '')
        file1.replace(')', '')
        file1.replace('{', '')
        file1.replace('}', '')
        file1.replace('[', '')
        file1.replace(']', '')
        file1.replace('%', '')
        file1.replace('char', '')
        file1.replace('printf', '')
        file1.replace('cout', '')
        file1.replace('cin', '')
        file1.replace('string', '')
        file1.replace('return', '')
        for s in all_submit:
            if s.id != source.id:
                file2 = open(str(s.path)).read()
                file2.replace('#include', '')
                file2.replace('int', '')
                file2.replace('float', '')
                file2.replace('int main', '')
                file2.replace('using namespace std', '')
                file2.replace(';', '')
                file2.replace('(', '')
                file2.replace(')', '')
                file2.replace('{', '')
                file2.replace('}', '')
                file2.replace('[', '')
                file2.replace(']', '')
                file2.replace('%', '')
                file2.replace('char', '')
                file2.replace('printf', '')
                file2.replace('cout', '')
                file2.replace('cin', '')
                file2.replace('string', '')
                file2.replace('return', '')
                # print(ld.leDistance(file1, file2))
                similar = int((1 - ld.leDistance(file1, file2) / (len(file1) + len(file2))) * 100)
                if similar > compare:
                    compare_name[n] = s.author
                    sim[n] = similar
                    compare = similar
        n += 1
    state = None
    homework = Homework.objects.get(id=homework_id)
    if request.user.is_authenticated():
        state = 'login'
        results = Submit.objects.filter(homework_id=homework_id)
        count = len(results)
        # print(sim)
        content = {
            'results': results,
            'count': count,
            'state': state,
            'user': request.user.first_name,
            'homework': homework,
            'permission': request.user.is_staff,
            'flag': 1,
            'compare': compare_name,
            'source': source_name,
            'similar': sim,
            'length': len(sim),
        }
    else:
        content = {
            'state': state,
            'homework': homework,
        }
    return render(request, 'homeworkdetails.html', content)
