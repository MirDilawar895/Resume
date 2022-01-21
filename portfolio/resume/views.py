from django.shortcuts import render
from .models import About
from .models import Skill, Testinomial, Project, Blog, Answerable,Booking
from django.contrib import messages
from django.core.mail import send_mail
from django.template import Template


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

        con = Booking(name=name, email=email, package=package, message=message)
        con.save()


        send_mail(

            
            'Thanks for sending me invitation for your Project !!. I have got your mail and  I will get to your very soon!',
            
            'hi'   +  name  +    'You have choice'    + package +     'package'
            

            'WE hope you will enjoy our services here.',
            'mirdilawar895@gmail.com',
            [email],
            fail_silently=False,

        )
        



        # message.success(request,'Data insert Succesfully')
    return render(request,'contact.html' )



