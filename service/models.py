from django.db import models


def upload_service_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


class Service(models.Model):
    name = models.CharField(max_length=100, blank=False)
    details = models.TextField()
    image = models.ImageField(upload_to=upload_service_image, blank=False)
    created = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Service List'


def upload_category_image(instance, filename):
    return "upload/{name}/{filename}".format(name=instance, filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False)
    image = models.ImageField(upload_to=upload_category_image, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Category List'
