from django.shortcuts import render



def myCv(request):
    return render(request,'cv.html',{})