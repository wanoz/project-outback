from django.db import models

# Create odels here.
class Usage_stats_local_db(models.Model):
    user_name = models.CharField(max_length=264)
    search_time = models.CharField(max_length=264)
    search_date = models.CharField(max_length=264)
    search_frequency = models.CharField(max_length=264)
    search_time_mean = models.CharField(max_length=264)
    search_time_stddev = models.CharField(max_length=264)
    search_date_interval_mean = models.CharField(max_length=264)
    search_date_interval_stddev = models.CharField(max_length=264)
    meat_1_last = models.CharField(max_length=264)
    meat_2_last = models.CharField(max_length=264)
    meat_3_last = models.CharField(max_length=264)
    veggie_1_last = models.CharField(max_length=264)
    veggie_2_last = models.CharField(max_length=264)
    veggie_3_last = models.CharField(max_length=264)
    carbs_1_last = models.CharField(max_length=264)
    carbs_2_last = models.CharField(max_length=264)
    dairy_1_last = models.CharField(max_length=264)
    dairy_2_last = models.CharField(max_length=264)
    dairy_3_last = models.CharField(max_length=264)
    gluten_free_last = models.CharField(max_length=264)
    halal_last = models.CharField(max_length=264)
    flavouring_last = models.CharField(max_length=264)
    restaurant_ID_last = models.CharField(max_length=264)
    
    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = "usage stats local database"