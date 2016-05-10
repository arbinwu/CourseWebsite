from django.shortcuts import render


# Create your views here.
def q_and_a(request):
    return render(request, 'q&a.html')
