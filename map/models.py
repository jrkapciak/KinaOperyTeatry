from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=128, verbose_name='Nazwa')
    lat = models.FloatField(blank=True)
    long = models.FloatField(blank=True)


    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name

class Shows(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    title = models.CharField(max_length=128, verbose_name='Tytuł')
    time = models.CharField(max_length=128,verbose_name='Czas')
    date = models.CharField(max_length=128, verbose_name='Data')
    place = models.ForeignKey(Place,blank=True, null=True)

    class Meta:
        ordering = ['title', ]

    def __str__(self):
        return self.title