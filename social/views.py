
from django.shortcuts import render

# Create your views here

def thanks(request):
    return render(request, 'social/thanks.html')

def welcome(request):
    return render(request, 'social/welcome.html')

def cancel(request):
    return render(request, 'social/cancel.html')

def howto(request):
    return render(request, 'social/howto.html')