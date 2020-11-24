from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def connect4(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('connect4'))
    return render(request,'connect4.html',{})
    
