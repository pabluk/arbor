from django.db import models


class Tree(models.Model):
    common_name = models.CharField(max_length=200)
    binomial_name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200, blank=True)
    photo = models.FileField(upload_to='photos', blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        return self.common_name

    def current_name(self):
        return self.name_set.order_by('-vote')[0]

class Name(models.Model):
    name = models.CharField(max_length=200)
    vote = models.PositiveIntegerField()
    tree = models.ForeignKey('Tree')

    def __unicode__(self):
        return self.name
