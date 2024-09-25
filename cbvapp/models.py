from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    ceo = models.CharField(max_length=50)
    origin = models.CharField(max_length=50)
    started_in = models.DateTimeField()
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    ram = models.PositiveIntegerField()
    battery = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    

    def __str__(self):
        return self.product_name