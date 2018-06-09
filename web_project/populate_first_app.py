import os
import django
import random
from first_app.models import Topic, AccessRecord, Webpage
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

# Fake population script
fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(header_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        # Get the topic for the entry
        header = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=header, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating complete!')