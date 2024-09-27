from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30, blank=False)
    short_description = models.TextField(blank=False, null=False)
    long_description = models.TextField(blank=True, null=True)
    date = models.DateField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)

    def __str__(self):
        return str(self.title)
