import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

import django
django.setup()

from map.models import Shows
from .items import ShowItem


class ScrapyOpera(object):
    def process_item(self, ShowItem, spider):
        # try:
        #     show = Shows.objects.get(identifier=item["id"])
        #     print( "Show already exist")
        #     return item
        # except Shows.DoesNotExist:
        #     pass

        show = Shows()
        show.title = ShowItem["title"]
        show.time = ShowItem["time"]
        show.date = ShowItem["date"]
        #show.place = "opera krakowska"
        show.save()
        #place = Place()
        #place.name = "opera krakowska"
        #place.save()



        return ShowItem


# def item_to_model(item):
#     model_class = getattr(item, 'django_model')
#     if not model_class:
#         raise TypeError("Item is not a `DjangoItem`")
#     return item.instance

# def get_or_create(model):
#     model_class = type(model)
#     created = False
#     try:
#         obj = model_class.objects.get(primary=model.primary)
#     except model_class.DoesNotExist:
#         created = True
#         obj = model
#
#     return (obj, created)
#
# from django.forms.models import model_to_dict
#
# def update_model(destination, source, commit=True):
#     pk = destination.pk
#
#     source_dict = model_to_dict(source)
#     for (key, value) in source_dict.items():
#         setattr(destination, key, value)
#
#     setattr(destination, 'pk', pk)
#
#     if commit:
#         destination.save()
#
#     return destination
#
# class ScrapyOpera(object):
#     def process_item(self, ShowItem, spider):
#         # try:
#         #      item_model = item_to_model(ShowItem)
#         # except TypeError:
#         #     return ShowItem
#         Shows, created = get_or_create(ShowItem)
#         try:
#             update_model(Shows, ShowItem)
#         except Exception as e:
#             return e
#         return ShowItem
#

