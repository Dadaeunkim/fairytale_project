from django.db import models
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.title}'
    
    def get_absolute_url(self):
        return f'/readingpage/{self.pk}'