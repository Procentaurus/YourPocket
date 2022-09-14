from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=30, null=True)
    avatar = models.ImageField(default='model.png', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

class Expense(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    name = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)

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
        return self.name+' - '+str(self.value)
        
    class Meta:
        ordering = ['-date_created']

class Income(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    name = models.CharField(max_length=50, null=True)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE)

    CATEGORIES = (
        ('Salary', 'Salary'),
        ('Return on investment', 'Return on investment'),
        ('Selling goods', 'Selling goods'),
        ('Credits and loans', 'Credit and loans'),
        ('Rent / pension', 'Rent / pension'),
        ('Bonus / Award', 'Bonus / Award'),
        ('Gifts', 'Gifts'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=30, choices=CATEGORIES)

    def __str__(self):
        return self.name+' - '+str(self.value)

    class Meta:
        ordering = ['-date_created']

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

    



