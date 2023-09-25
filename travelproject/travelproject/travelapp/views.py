
from django.shortcuts import render
from.models import Place
from.models import Owner
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    head=Owner.objects.all()
    return render(request,"index.html", {'result': obj , 'owner':head})

def register(request):
    return render(request,"register.html")

# def value(request):
#     return render(request,"index.html")