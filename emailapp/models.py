from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email_address = models.EmailField()
    customer_status = (('active', 'active',),('inactive','inactive'))
    status = models.CharField(max_length=50,choices=customer_status,default='active')
    
    def __str__(self):
        return self.name