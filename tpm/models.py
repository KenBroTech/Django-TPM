from django.db import models

# Create your models here.


class ComputerDB(models.Model):

    status = (
        ('P', 'P'),
        ('R', 'R'),
    )

    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    registration_status = models.CharField(
        max_length=10, choices=status, null=True)
    registration_date = models.DateField(auto_now_add=True)
