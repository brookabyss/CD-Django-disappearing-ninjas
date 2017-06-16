from django.shortcuts import render,redirect, HttpResponse

def index(request):
    return render(request,'ninja/index.html')

def show(request):
    return render(request, 'ninja/show.html')

def show_color(request,color):
    context={
        'ninja': "ninja/images/notapril.jpg"
    }
    if color=="blue":
        context['ninja']= "ninja/images/leonardo.jpg"
    elif color=="orange":
        context['ninja']= "ninja/images/michelangelo.jpg"
    elif color=="red":
        context['ninja']= "ninja/images/raphael.jpg"
    elif color=="purple":
        context['ninja']= "ninja/images/donatello.jpg"

    return render(request,'ninja/color.html', context)
