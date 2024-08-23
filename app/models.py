from django.db import models
from django.utils import timezone

LOCATION_CHOICES = [
    ('top', 'Top'),
    ('left', 'Left'),
    ('right', 'Right'),
    ('bottom', 'Bottom'),
]

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
    


class Location(models.Model):
    locationid= models.AutoField(primary_key=True)
    locationname=models.CharField(max_length=25)
    CreatedAt = models.DateField(default=timezone.now)
    UpdatedAt=models.DateField(default=timezone.now)

    def __str__(self):
        return self.locationname    


class TrekPlan(models.Model):
    TrekPlanID=models.AutoField(primary_key=True)
    Trekid=models.CharField(max_length=100)
    TrekDay=models.CharField(max_length=100)
    TrekPlanTitle=models.CharField(max_length=100)
    TrekplanDescription=models.CharField(max_length=600)


    def __str__(self):
        return self.TrekPlanTitle
    

class Trekcategory(models.Model):
    Trekcategoryid=models.AutoField(primary_key=True)
    TrekCategory=models.CharField(max_length=100)

    def __str__(self):
        return self.TrekCategory

class TrekHeroImages(models.Model):
    TrekHeroImagesid=models.AutoField(primary_key=True)
    Location=models.CharField(max_length=6, choices=LOCATION_CHOICES, default='top')
    TrekHeroImagesUrl=models.CharField(max_length=100) 


    def __str__(self):
        return self.TrekHeroImagesUrl


class ThingsToCarry(models.Model):
    ThinksToCarryid=models.AutoField(primary_key=True)
    Description=models.CharField(max_length=1000)


    def __str__(self):
        return self.Description



class Trek(models.Model):
    Trekid=models.AutoField(primary_key=True)
    Trek_category=models.ForeignKey(Trekcategory, on_delete=models.CASCADE, related_name='Trekcategory')
    LocationTag=models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Location')
    RegularPrice=models.DecimalField(max_digits=10, decimal_places=2)
    DicountedPrice=models.DecimalField(max_digits=10, decimal_places=2)
    TotalDuration=models.DecimalField(max_digits=10, decimal_places=2)
    TotalDay=models.IntegerField()
    TotalNight=models.IntegerField()
    TrekHeight=models.DecimalField(max_digits=10, decimal_places=2)
    TrekDistance=models.DecimalField(max_digits=10, decimal_places=2)
    Pickupfrom=models.CharField(max_length=100)
    DropTo=models.CharField(max_length=100)
    TrekHeroImage=models.ForeignKey(TrekHeroImages, on_delete=models.CASCADE, related_name='TrekHeroImages')
    Overview=models.CharField(max_length=100,null=True)
    Highlights=models.CharField(max_length=1000)
    ThingsToCarryid=models.ForeignKey(ThingsToCarry, on_delete=models.CASCADE, related_name='ThingsToCarry')
    TrekGallery=models.ImageField()
    MeetingPoint=models.CharField(max_length=200)    

    
    def __str__(self):
       return self.Overview   