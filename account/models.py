from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField()
    email = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.username