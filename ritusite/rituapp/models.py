from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)
    
    class Meta:
        ordering = ["title"]
    def __str__(self):
        return f"Title is: {self.title}"

class Article(models.Model):
    headline = models.CharField(max_length=50)
    Publications = models.ManyToManyField(Publication)
    
    class Meta:
        ordering = ["headline"]
    def __str__(self):
        return f"Headline is: {self.headline}"
    