from django.db import models
from main.helpers import parse_row


class Person(models.Model):
    phone_one = models.CharField(max_length=30)
    phone_two = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        parse_row(self)
        super(Person, self).save(force_insert, force_update, using, update_fields)
