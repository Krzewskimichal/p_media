from django.db import models
from django.dispatch import receiver

import os


class Publisher(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64)
    birthdate = models.DateField(blank=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    pages_num = models.IntegerField()
    cover_image = models.ImageField(upload_to='cover_images/')

    def __str__(self):
        return self.title


@receiver(models.signals.post_delete, sender=Book)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.cover_image:
        if os.path.isfile(instance.cover_image.path):
            os.remove(instance.cover_image.path)


@receiver(models.signals.pre_save, sender=Book)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).cover_image
    except sender.DoesNotExist:
        return False

    new_file = instance.cover_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
