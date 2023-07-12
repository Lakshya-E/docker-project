from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

CATEGORY_GAMES = (
    ('AG', 'Action Games'),
    ('AD', 'Adventure Games'),
    ('HG', 'Horror Games'),
    ('SG', 'Survival Games'),
    ('ZG', 'Zombie Games')
)

class GameProduct(models.Model):
    """This class is the model to game product"""
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    original_price = models.FloatField()
    selling_price = models.FloatField()
    description = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_GAMES, max_length=2)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name
    

User = get_user_model()

class UserProfile(models.Model):
    """This function creates User after authentication"""
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username.username 