from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# database will be managed by the Integrated MYSQL DBMS implicitly by Django Framework
# here we are creating the database only using the class 
# name of table/realtion in database will be the name of table 
# variables inside the class will be attributes of relation/table  
# all the objects of a class will the tuple/row of ralation/table
# we will create the tuple using the class object 
#  we will use the class_form to recieve the details of on object and on saving the object
   # it will add the object inside the table as a tuple...

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    id=models.AutoField(primary_key=True)
    dp=models.ImageField(max_length=200,upload_to='images/')
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=200)
    dept=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    education=models.CharField(max_length=200,blank=True)
    guide=models.TextField(max_length=700)
    def __str__(self):
         return self.name

class Subject(models.Model):
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    subject_date=models.DateTimeField(auto_now=True)
    subject_name=models.CharField(max_length=200)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=20)

    def __str__(self):
        return self.subject_name

class Unit(models.Model):
    unit_subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    unit_name=models.CharField(max_length=200)
    unit_imp=models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return self.unit_name

class Topic(models.Model):
    unit_topic=models.ForeignKey(Unit,on_delete=models.CASCADE)
    topic_date=models.DateTimeField(auto_now=True)
    topic_name=models.CharField(max_length=200)
    topic_weightage=models.TextField(max_length=1000,blank=True)
    file=models.FileField(max_length=100,upload_to='topic_files/')
    topic_link=models.URLField(null=True,blank=True)

    def __str__(self):
        return self.topic_name
    class Meta:
        ordering=['-topic_date']
