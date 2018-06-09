from django.db import models

# Create models here.
class Meals_local_db(models.Model):
    meal_name = models.CharField(max_length=264)
    price = models.CharField(max_length=264)
    hot_or_cold = models.CharField(max_length=264)
    cuisine_type = models.CharField(max_length=264)
    meal_category = models.CharField(max_length=264)
    cooking_method = models.CharField(max_length=264)
    meat_1 = models.CharField(max_length=264)
    meat_2 = models.CharField(max_length=264)
    meat_3 = models.CharField(max_length=264)
    carbs_1 = models.CharField(max_length=264)
    carbs_2 = models.CharField(max_length=264)
    veggie_1 = models.CharField(max_length=264)
    veggie_2 = models.CharField(max_length=264)
    veggie_3 = models.CharField(max_length=264)
    dairy_1 = models.CharField(max_length=264)
    dairy_2 = models.CharField(max_length=264)
    dairy_3 = models.CharField(max_length=264)
    dairy_4 = models.CharField(max_length=264)
    gluten_free = models.CharField(max_length=264)
    halal = models.CharField(max_length=264)
    flavouring = models.CharField(max_length=264)
    restaurant_ID = models.CharField(max_length=264)

    def __str__(self):
        return self.meal_name

    class Meta:
        verbose_name_plural = "meals local database"

# class Topic(models.Model):
#     header_name = models.CharField(max_length=264, unique=True)

#     def __str__(self):
#         return self.header_name

# class Webpage(models.Model):
#     topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
#     name = models.CharField(max_length=264, unique=True)
#     url = models.URLField(unique=True)

#     def __str__(self):
#         return self.name

# class AccessRecord(models.Model):
#     name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING)
#     date = models.DateField()

#     def __str__(self):
#         return str(self.date)
