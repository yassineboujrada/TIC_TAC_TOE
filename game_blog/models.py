from django.db import models

# Create your models here.

class login_test(models.Model):
    first_name = models.CharField(max_length=100)
    email = models.EmailField()
    password=models.CharField(max_length=20)

    def __str__(self):
        return f'{self.email} + {self.password}'