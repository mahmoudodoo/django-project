from django.shortcuts import render



def connect4(request):
    return render(request,'connect4.html',{})