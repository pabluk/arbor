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
        """Return the name selected for votes."""
        return self.name_set.order_by('-vote')[0]

    def assign_names(self):
        """Assign 3 random avaliable names."""
        if self.name_set.count() == 0:
            name = Name.objects.filter(tree__isnull=True, gender=GENDER_FEMALE).order_by('?')[0]
            name.tree = self
            name.save()

            name = Name.objects.filter(tree__isnull=True, gender=GENDER_MALE).order_by('?')[0]
            name.tree = self
            name.save()

            name = Name.objects.filter(tree__isnull=True).order_by('?')[0]
            name.tree = self
            name.save()

    def votes(self):
        """Return names and votes."""
        vote_list = ["%s (%s)" % (n.name, n.vote) for n in self.name_set.all()]
        return " / ".join(vote_list)

class Name(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    vote = models.PositiveIntegerField(default=0)
    tree = models.ForeignKey('Tree', blank=True, null=True)

    def __unicode__(self):
        return self.name
