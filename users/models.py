from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    age= models.IntegerField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
      return self.name