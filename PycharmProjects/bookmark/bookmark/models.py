from django.db import models
from django.urls import reverse
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site url')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return "site name : "+self.site_name+", url : "+self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])