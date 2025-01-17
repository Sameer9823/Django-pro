from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('B', 'Black'),
        ('W', 'White'),
        ('G', 'Green'),
        ('R', 'Rooibos'),
        ('C', 'Cinnamon'),
        ('P', 'Peppermint'),
        
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    price = models.CharField(max_length=10, default='Rs. 100')
    
    def __str__(self):
        return self.name
    

# one to many
class chaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE , related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'
    
#many to many
class Store(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')
    
    def __str__(self):
        return self.name
    
#one to one
class Chaicertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=20)
    issue_date = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.chai.name} Certificate'
    
