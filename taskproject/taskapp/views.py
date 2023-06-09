from django.http import HttpResponse
from django.shortcuts import render
from .models import table,profiletable


# Create your views here.
def web(request):
    obj=table.objects.all()
    obj2=profiletable.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj2})

def index(request):
    return render(request,'index.html')




# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     sum=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'result1':sum,'result2':sub,'result3':mul,'result4':div})
# def about(request):
#     return HttpResponse("about")
# def contact(request):
#     return render(request,'contact.html')
# def detail(request):
#     return HttpResponse("detail")
# def thanks(request):
#     return render(request,'thanks.html')







