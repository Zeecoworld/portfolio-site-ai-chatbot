from django.db import models

# Create your models here.





class Enquiry(models.Model):
    firstname = models.CharField(blank=False, max_length=30)
    lastname = models.CharField(blank=False, max_length=30)
    email = models.EmailField(blank=False)
    services = models.CharField(blank=False, max_length=30)
    message = models.TextField(blank=False)


    def __str__(self):
        return f'{self.firstname}-{self.lastname}-{self.email}-{self.services}-{self.message}'

