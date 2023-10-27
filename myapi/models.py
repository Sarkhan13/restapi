from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    active = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)
    
    
