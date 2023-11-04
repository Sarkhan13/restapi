from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    about = models.TextField()

    def __str__(self):
        return f'{self.name} {self.surname}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    text = models.TextField()
    active = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.title)
    
    
