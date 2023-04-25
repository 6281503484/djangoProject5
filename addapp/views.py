from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def input(request):
    return render(request,'input.html')
def add(request):
    x=request.GET["t"]
    y=request.GET["t2"]
    i=int(x)
    j=int(y)
    k=i+j
    res=HttpResponse("the sum is="+ str(k))
    return res
