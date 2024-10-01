from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=500, blank=False)
    abstract = models.TextField(blank=False, null=True)
    pub_url = models.CharField(max_length=200, blank=True)
    citation = models.CharField(max_length=200, blank=True)
    author = models.TextField(blank=True, null=True)
    pub_year = models.IntegerField(blank=True, null=True)    

    def __str__(self):
        return str(self.title)
