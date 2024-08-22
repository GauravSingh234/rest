from django.db import models

class students(models.Model):
    Name = models.CharField(max_length=100)
    fathers_name= models.CharField(max_length=100)
    mothers_name=models.CharField(max_length=100)
    age=models.CharField(max_length=15)
    address=models.CharField(max_length=150)
    pincode=models.IntegerField()
    mobile=models.IntegerField()


    def __str__(self):
        return self.Name
