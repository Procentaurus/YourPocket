from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)
    avatar = models.ImageField(null=True)#default

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Expense(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    CATEGORIES = (
        ('Home','Home'),
        ('Health','Health'),
        ('Entertainment','Entertainment'),
        ('Transport', 'Transport'),
        ('Taxes and Fees', 'Taxes and Fees'),
        ('Clothes', 'Clothes'),
        ('Food', 'Food'),
        ('Credits and loans', 'Credits and loans'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self):
        return self.name+' - '+self.value

class Income(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    CATEGORIES = (
        ('Salary', 'Salary'),
        ('return on investment', 'return on investment'),
        ('Selling goods', 'Selling goods'),
        ('Credits and loans', 'Credit and loans'),
        ('Rent / pension', 'Rent / pension'),
        ('Bonus / Award', 'Bonus / Award'),
        ('Gifts', 'Gifts'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self):
        return self.name+' - '+self.value

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultant = models.ForeignKey(User,on_delete=models.CASCADE, related_name='consultant')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['created']
    
    def __str__(self):
        if len(self.body) > 100:
            return self.body[0:100]+" ..."
        else:
            return self.body

    



