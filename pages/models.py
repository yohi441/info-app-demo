from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Faculty(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)


class SchoolMap(models.Model):
    name = models.CharField(max_length=200)
    map_photo = models.ImageField(upload_to='img', blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)
    map_description = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Office(models.Model):
    name = models.CharField(max_length=200)
    map_photo = models.ImageField(upload_to='img', blank=True, null=True)
    photo = models.ImageField(upload_to='img', blank=True, null=True)
    


    def __str__(self):
        return self.name


class StaffMember(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    middle_initial = models.CharField(max_length=1, null=True, blank=True)
    office = models.ForeignKey(Office, on_delete=models.CASCADE, related_name='office')
    position = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.name, self.lastname)




class FrequentlyAskedQuestion(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    map_photo = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.title


    



