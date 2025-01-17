from django.db import models
from django.utils import timezone

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
    
