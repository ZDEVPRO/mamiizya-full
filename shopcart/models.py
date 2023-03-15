from django.db import models
from home.models import *


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        if self.product and self.user:
            return f"{self.product.title} - {self.user.first_name} {self.user.last_name}"
        else:
            self.delete()

    @property
    def price(self):
        if self.product:
            return self.product.price
        else:
            self.delete()

    @property
    def amount(self):
        if self.product:
            return int(self.quantity) * int(self.product.price)
        else:
            return 0


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    first_name = models.CharField('Ism', max_length=1000)
    last_name = models.CharField('Familya', max_length=1000)
    phone_number = models.CharField('Telefon raqam', max_length=1000)

    region = models.CharField('Viloyat', max_length=1000)
    district = models.CharField(max_length=1000)
    address = models.TextField()
    client_notes = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.region}"

    class Meta:
        verbose_name = 'Buyurtma'
        verbose_name_plural = 'Buyurtmalar'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    title = models.CharField('Nomi', max_length=600)
    price = models.CharField('Narxi', max_length=600)
    image = models.ImageField(upload_to='products/')
    quantity = models.IntegerField('Miqdori')

    color = models.CharField('Rangi', max_length=600)
    size = models.CharField("O'lchami", max_length=600)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Buyurtma Maxsuloti'
        verbose_name_plural = 'Buyurtma Maxsulotlari'

    def image_tag(self):
        return mark_safe(f"<img src='{self.image.url}' height='50'>")

    def image_tag_big(self):
        return mark_safe(f"<img src='{self.image.url}' height='300'>")

    def view_image(self):
        return mark_safe(f"<a href='{self.image.url}'><h4>RASMNI KO'RISH</h4></a>")

    @property
    def amount(self):
        return int(self.quantity) * int(self.price)

    def Jami_Narxi(self):
        return int(self.quantity) * int(self.price)
