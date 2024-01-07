from django.db import models

class Student(models.Model):
    s_name = models.CharField(max_length=256, null=False)
    s_email = models.EmailField(max_length=256, null=True)
    s_contact = models.BigIntegerField()

    # def __str__(self):
    #     self.s_name

class Course(models.Model):
    c_name = models.CharField(max_length=512)

    # def __str__(self):
    #     self.c_name
