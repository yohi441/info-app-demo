from django.db import models


class FacultyIteDepartment(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img')


    def __str__(self):
        return self.name

class FacultyHrmDepartment(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name

class SchoolMap(models.Model):
    name = models.CharField(max_length=200)
    map_photo = models.ImageField(upload_to='img', blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length=200)
    map_photo = models.ImageField(upload_to='img', blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name


class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title

    


    



