from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create a user's profile model

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=9, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zipcode = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    bank_account_code = models.CharField(max_length=26, blank = True)
    image = models.ImageField(upload_to='uploads/users', default="{% static 'images/userimage.png' %}")

    def __str__(self):
        return self.user.username
    

# Create user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender= User)

# Create a category model

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name_plural = "categories"

# Create a puzzle model 

class Puzzle(models.Model):
    CONDITION_CHOICES= [
        ('Nowy', 'Nowy'),
        ('Bardzo dobry', 'Bardzo dobry'),
        ('Dobry', 'Dobry'),
        ('Średni', 'Średni'),
        ('Zły', 'Zły'),
    ]
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2500, default='', blank= True, null = True)
    brand = models.CharField(max_length=50)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=7)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    condition = models.CharField(max_length=12, choices=CONDITION_CHOICES, default='Bardzo dobry')
    image = models.ImageField(upload_to='uploads/puzzles')
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
