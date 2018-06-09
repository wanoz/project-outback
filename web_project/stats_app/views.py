from django.shortcuts import render
from django.http import HttpResponse
from stats_app.models import Usage_stats_local_db

# Create views (controller)
def page_stats(request):
    # Get the data objects
    usage_stats = Usage_stats_local_db.objects.values()

    # Set Django template tag dictionary
    usage_stats_tagdict = {'usage_stats_key' : usage_stats}

    return render(request, 'stats_app/page_stats.html', context=usage_stats_tagdict)