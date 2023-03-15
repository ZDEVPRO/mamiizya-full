from django.db import models
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class Section1(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "1-Bolim"
        verbose_name_plural = "1-Bolim"

    def image_tag(self):
        return mark_safe(f"<img src='{self.background_image.url}' height='50'")


class Section2(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "2-Bolim"
        verbose_name_plural = "2-Bolim"

    def image_tag(self):
        return mark_safe(f"<img src='{self.background_image.url}' height='50'")


class Section3(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "3-Bolim"
        verbose_name_plural = "3-Bolim"

    def image_tag(self):
        return mark_safe(f"<img src='{self.background_image.url}' height='50'")


class Section4(models.Model):
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')

    button_title = models.CharField(max_length=300)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "4-Bolim"
        verbose_name_plural = "4-Bolim"

    def image_tag(self):
        return mark_safe(f"<img src='{self.background_image.url}' height='50'")


class Section5to8(models.Model):
    button_title = models.CharField(max_length=1000)
    button_link = models.CharField(max_length=1000)

    background_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.button_title

    class Meta:
        verbose_name = "Bo'lim 5-dan 8-gacha"
        verbose_name_plural = "Bo'lim 5-dan 8-gacha"


class Section9to10(models.Model):
    title = RichTextField()
    subtitle = models.CharField(max_length=1000)
    background_image = models.ImageField(upload_to='images/')
    button_name = models.CharField(max_length=600)
    button_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bo'lim 9-dan 10-gacha"
        verbose_name_plural = "Bo'lim 9-dan 10-gacha"


class Section11Plus(models.Model):
    title = models.CharField(max_length=600)
    price = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bo'lim 11+"
        verbose_name_plural = "Bo'lim 11+"
