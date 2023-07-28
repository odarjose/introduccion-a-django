from django.db import models

# Create your models here.
#es para tu django admin o panel de admin
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    
    def __str__(self):
        return self.title
