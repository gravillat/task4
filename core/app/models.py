from django.db import models


class Branch(models.Model):
    latitude = models.CharField(max_length=125)
    longitude = models.CharField(max_length=125)
    address = models.CharField(max_length=125)

    def __str__(self):
        return self.address


class Contact(models.Model):
    type_contact = models.SmallIntegerField(
        choices=(
            (1, 'phone'),
            (2, 'facebook'),
            (3, 'email')
        )
    )
    value = models.CharField(max_length=125)

class Category(models.Model):
    name = models.CharField(max_length=125)
    imgpath = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='media/images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    branches = models.ManyToManyField(Branch)
    contacts = models.ManyToManyField(Contact)

    def __str__(self):
        return self.name



