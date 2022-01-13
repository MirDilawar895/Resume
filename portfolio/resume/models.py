from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=50, null=True)
    description = RichTextField()
    def __str__(self):
        return self.name
    

class Skill(models.Model):
    technology_name= models.CharField(max_length=50, null=True)
    technology_decs = RichTextField()
    def __str__(self):
        return self.technology_name

class Testinomial(models.Model):
    testinomial_content = RichTextField()
    testinomial_image = models.ImageField(upload_to='photos/%y/%m/%d/')
    testinomial_name = models.CharField(max_length=50, null=True)
    testinomial_info= models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.testinomial_name
    


class Project(models.Model):
    project_image = models.ImageField(upload_to='photos/%y/%m/%d/')
    project_name = models.CharField(max_length=50, null=True)
    project_desc = RichTextField()
    project_client = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.project_name
    

class Blog(models.Model):
    blog_image = models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_name = models.CharField(max_length=50, null=True)
    blog_desc = RichTextField()
    project_footer = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.blog_name








