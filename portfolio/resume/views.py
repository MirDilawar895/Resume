from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def portfolio(request):
    return render(request,'portfolio.html' )

def service(request):
    return render(request,'service.html' )


def resume(request):
    return render(request,'resume.html' )

def blog(request):
    return render(request,'blog.html' )

def contact(request):
    return render(request,'contact.html' )


def project(request):
    return render(request, 'project.html')

def content(request):
    return render(request, 'content.html')

def alting(request):
    return render(request, 'alting.html')
