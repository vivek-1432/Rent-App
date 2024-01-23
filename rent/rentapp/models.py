from django.db import models

class prod(models.Model):
    name = models.CharField(max_length = 50)
    product = models.CharField(max_length=50)
    price = models.FloatField()
    date = models.DateField()
    till = models.DateField()
    image = models.ImageField(upload_to= 'images/')


    def __str__(self):
        return self.name