from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    message = models.TextField()
    date = models.DateField()


class IceCream(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image_url = models.URLField(blank=True, null=True)  # optional, for images

    def __str__(self):
        return self.name


# Wishlist model
class Wishlist(models.Model):
    items = models.ManyToManyField('IceCream', blank=True)  # string notation for forward reference

    def __str__(self):
        return f"Wishlist {self.id}"


# Cart model
class Cart(models.Model):
    items = models.ManyToManyField('IceCream', blank=True)  # string notation

    def __str__(self):
        return f"Cart {self.id}"
