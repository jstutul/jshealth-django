from django.db import models


# Create your models here.
def upload_client_say_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


def upload_about_us_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


class ClientSay(models.Model):
    name = models.CharField(max_length=30)
    degisnation = models.TextField(max_length=300)
    image = models.ImageField(upload_to=upload_client_say_image, blank=False)


class AboutUs(models.Model):
    name = models.CharField(max_length=30)
    degisnation = models.TextField(max_length=300)
    image = models.ImageField(upload_to=upload_about_us_image, blank=False)
