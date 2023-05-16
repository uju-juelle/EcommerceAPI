from django.db import models



CATEGORY_CHOICES = (
    ("MEN", "MEN"),
    ("WOMEN", "WOMEN"),
    ("CHILDREN", "CHILDREN"),
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=100)
    image = models.ImageField(upload_to="product_images") 


    def __str__(self):
        return self.name
