from django.shortcuts import render


# Create your views here.
def view(request):
    return render(request, 'forum.html')


def topic(request):
    return render(request, 'topic.html')
