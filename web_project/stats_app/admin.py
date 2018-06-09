from django.contrib import admin
from stats_app.models import Usage_stats_local_db as db

# Register your models here.
admin.site.register(db)
