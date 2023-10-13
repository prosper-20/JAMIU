from django.db import models
from users.models import Userprofile
from django.db import models


class Property(models.Model):
    # Agent = models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    # title  = models.CharField(max_length=100)
    #  location = models.CharField(max_length=250)
    # price = models.DecimalField(max_digits=13, decimal_places=2)
    # image = models.ImageField(upload_to='property_image/')
    # description = models.TextField()
    # image1 = models.ImageField(upload_to='property_image/',null=True)
    # image2 = models.ImageField(upload_to='property_image/',null=True)
    # image3 = models.ImageField(upload_to='property_image/',null=True)
    # image4 = models.ImageField(upload_to='property_image/',null=True)
    # image5 = models.ImageField(upload_to='property_image/',null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    property_type_choices = [
         ('house', 'House'),
         ('apartment', 'Apartment'),
         ('condo', 'Condo'),
         ('land', 'Land'),
    ]
    
    Agent = models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=property_type_choices)
    location = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property_photos/')
    image1 = models.ImageField(upload_to='property_photos/', blank=True, null=True)
    image2 = models.ImageField(upload_to='property_photos/', blank=True, null=True)
    image3 = models.ImageField(upload_to='property_photos/', blank=True, null=True)
    image4 = models.ImageField(upload_to='property_photos/', blank=True, null=True)
    image5 = models.ImageField(upload_to='property_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Property"

class Agent(models.Model):
    name = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='agent_photos/')

    def _str_(self):
        return self.name
    class Meta:
        verbose_name_plural = "Agent"


class Listing(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField()
    sold_date = models.DateField(null=True, blank=True)

    def _str_(self):

        return f"{self.property.title} - {self.agent.name}"
    
    class Meta:
        verbose_name_plural = "Listing"





class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    inquiry_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Inquiry for {self.property.title} by {self.name}"
    
    class Meta:
        verbose_name_plural = "Inquiry"



