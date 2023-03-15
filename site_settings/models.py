from django.db import models
from django.utils.safestring import mark_safe


class HomeSlider(models.Model):
    subtitle = models.CharField(max_length=600)
    title = models.TextField()
    background_image = models.ImageField(upload_to='images/')
    button_name = models.CharField(max_length=600)
    button_link = models.CharField(max_length=6000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Home Slider'
        verbose_name_plural = 'Home Slider'


class About(models.Model):
    big_title = models.TextField()
    title = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    button_title = models.CharField(max_length=600)
    button_link = models.CharField(max_length=3000)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="70">'.format(self.image.url))

    class Meta:
        verbose_name = 'Biz haqimizda'
        verbose_name_plural = 'Biz haqimizda'


class ContactData(models.Model):
    phone1 = models.CharField(max_length=600)
    phone2 = models.CharField(max_length=600)
    email = models.CharField(max_length=600)
    address = models.TextField()
    working_time = models.CharField(max_length=10000)

    telegram = models.CharField(max_length=1000)
    instagram = models.CharField(max_length=1000)
    whatsapp = models.CharField(max_length=1000)

    def __str__(self):
        return self.phone1

    class Meta:
        verbose_name = 'Aloqa Malumotlari'
        verbose_name_plural = 'Aloqa Malumotlari'


class TelegramBot(models.Model):
    chat_id = models.CharField(max_length=1000)
    bot_token = models.CharField(max_length=1000)

    def __str__(self):
        return self.chat_id

    class Meta:
        verbose_name = 'Telegram Bot'
        verbose_name_plural = 'Telegram Bot'
