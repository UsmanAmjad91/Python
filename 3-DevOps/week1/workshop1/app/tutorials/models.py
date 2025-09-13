from django.db import models
class Tutorial(models.Model):
    title = models.CharField(max_length=200)
    tutorial_url = models.URLField()
    image_path = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self): return self.title
