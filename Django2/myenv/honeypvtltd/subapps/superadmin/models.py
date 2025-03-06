from django.db import models

# Create your models here.

class Superadmin_data(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    
class Manager_data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    birth_date=models.DateField()
    joining_date=models.DateField()
    emp_id=models.CharField(max_length=10)
    def __str__(self):
        return self.name
    
class Manager_image(models.Model):
    fkey= models.ForeignKey(to=Manager_data, on_delete=models.CASCADE)
    pan_card=models.CharField(max_length=10)
    aadhar_card=models.CharField(max_length=12)
    address=models.CharField(max_length=150)
    image=models.ImageField(default=True,null=True,upload_to='image/')
    
    
    