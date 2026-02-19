from django.db import models
from django.contrib.auth.models import User

class AlumniProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    passout_year = models.IntegerField()
    register_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    current_job = models.CharField(max_length=100, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.png')


    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    




    





