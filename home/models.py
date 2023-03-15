from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.utils.safestring import mark_safe
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username yozilish kerak!")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):
    email = None
    phone = models.CharField(max_length=60, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def save(self, *args, **kwargs):
        if 80 > len(self.password):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Color(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rang'
        verbose_name_plural = 'Ranglar'


class Size(models.Model):
    title = models.CharField(max_length=600)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "O'lcham"
        verbose_name_plural = "O'lchamlar"


class Product(models.Model):
    title = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size)
    color = models.ManyToManyField(Color)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    content = RichTextField()
    additional_description = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50">'.format(self.image.url))

    class Meta:
        verbose_name = 'Maxsulot'
        verbose_name_plural = 'Maxsulotlar'


class ImageItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title


class Contact(models.Model):
    first_name = models.CharField(max_length=600)
    last_name = models.CharField(max_length=600)
    phone = models.CharField(max_length=600)
    message = models.TextField()
    ip = models.CharField(max_length=600)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = "Aloqa bo'limi"
        verbose_name_plural = "Aloqa bo'limi"
