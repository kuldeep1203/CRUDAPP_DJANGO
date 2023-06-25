from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''function to handle the traffic of the home page  it will basically be the first page'''
def home(request):
    return render(request,'home.html')


def about(request):
    return HttpResponse('<h1>About</h1>')

def hp(request):
    return render(request,'hp.html')