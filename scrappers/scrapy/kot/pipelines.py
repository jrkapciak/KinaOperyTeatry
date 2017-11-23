import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

import django
django.setup()

from map.models import Shows
from map.models import Place
from .items import ShowItem


from map.models import Shows, Place
from .items import ShowItem


class ScrapyOpera(object):
    def process_item(self, ShowItem, spider):
        place, created = Place.objects.get_or_create(name="opera krakowska")

        show = Shows.objects.update_or_create(
            time=ShowItem["time"],
            date=ShowItem["date"],
            place=place,
            defaults={'title': ShowItem["title"]}
        )

        return ShowItem

