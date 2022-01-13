from django.shortcuts import render
from .models import About
from .models import Skill, Testinomial, Project, Blog
# Create your views here.

def home(request):
    about = About.objects.all()
    skill = Skill.objects.all()
    testinomial = Testinomial.objects.all()
    project = Project.objects.all()
    blog = Blog.objects.all()
    data = {
        'about': about,
        'skill': skill,
        'testinomial': testinomial,
        'project': project,
        'blog':blog,
    }
    return render(request, 'home.html', data)


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
