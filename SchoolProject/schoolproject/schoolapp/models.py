from django.db import models

# Create your models here.

class Department(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
         return self.name

class Course(models.Model):
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class store(models.Model):
    username=models.CharField(max_length=50)
    date=models.DateTimeField
    age=models.IntegerField(max_length=2)
    GENDER_CHOICES=(('M','male'),('F','female'))
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES)
    number=models.IntegerField(max_length=10)
    email=models.EmailField
    address=models.TextField(max_length=250)
    dept=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.username
