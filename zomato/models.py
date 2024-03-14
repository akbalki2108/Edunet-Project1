from django.db import models
from django.utils.translation import gettext as _


class Restaurant(models.Model):
    url = models.URLField(max_length=1000000)
    name = models.CharField(max_length=50000)
    online_order = models.BooleanField(default=False)
    book_table = models.BooleanField(default=False)
    rate = models.FloatField()
    votes = models.IntegerField()
    location = models.CharField(max_length=50000)
    rest_type = models.CharField(max_length=50000)
    cuisines = models.CharField(max_length=50000)
    cost2plates = models.FloatField()
    listed_in_type = models.CharField(max_length=50000)
    area = models.CharField(max_length=50000)
    ratings = models.CharField(max_length=300000)
    reviews = models.CharField(max_length=1000000)
    count = models.IntegerField()
    sentiments = models.CharField(max_length=1000000)
    summaries = models.CharField(max_length=1000000)
    sentiment_label = models.CharField(max_length=50000)
    index_f = models.IntegerField()

    def __str__(self):
        return self.name