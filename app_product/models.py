from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    price = models.IntegerField()
    type = models.CharField(max_length=10,choices=(('tv.','Tv'),
                                                   ('screen','Screen'))) # use tuple to can insert more choices
    img = models.ImageField(upload_to='products')



    def __str__(self):
        return 'Product: ' + self.name