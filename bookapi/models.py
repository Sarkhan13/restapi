from django.db import models



class Book(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    createddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

