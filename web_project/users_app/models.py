from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_profile_db(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields
    vegetarian = models.CharField(max_length=264)
    food_allergy = models.CharField(max_length=264)

    def __str__(self):
        return self.user_profile.username

    class Meta:
        verbose_name_plural = "users profile local database"