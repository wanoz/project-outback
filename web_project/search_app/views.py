from django.shortcuts import render
from django.http import HttpResponse

# Create views (controller)
def page_search(request):
    return render(request, 'search_app/page_search.html')