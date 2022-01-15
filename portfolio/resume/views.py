from django.shortcuts import render
from .models import About
from .models import Skill, Testinomial, Project, Blog, Answerable


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
    about = About.objects.all()
    project = Project.objects.all()
    data = {
'about': about,
'project': project,
    }
    return render(request,'portfolio.html',data )

def service(request):
    answerable = Answerable.objects.all()
    data ={
        'answerable':answerable,
    }
    return render(request,'service.html',data )


def resume(request):
    about = About.objects.all()
    project = Project.objects.all()

    data = {
        'about': about,
        'project': project,
    }
    return render(request,'resume.html',data  )

def blog(request):
    blog = Blog.objects.all()
    data = {
        'blog': blog,

    }
    return render(request,'blog.html', data )

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        package = request.POST['package']
        message = request.POST['message']

        con = Contact(name=name, email=email, package=package, message=message)
        con.save()
        message.success(request,'Data insert Succesfully')
    return render(request,'contact.html' )



