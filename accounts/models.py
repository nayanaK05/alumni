from django.db import models
from django.contrib.auth.models import User

class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    department = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    register_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)

    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

