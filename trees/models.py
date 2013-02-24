from django.db import models

GENDER_MALE = 'm'
GENDER_FEMALE = 'f'

GENDER_CHOICES = (
    (GENDER_FEMALE, u'Fille'),
    (GENDER_MALE, u'Gar\xe7on'),
)


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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    vote = models.PositiveIntegerField(default=0)
    tree = models.ForeignKey('Tree', blank=True, null=True)

    def __unicode__(self):
        return self.name
