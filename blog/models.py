from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default="Some")

    def __str__(self):
        return self.title

    def getDetail(self):
        return f'Title: {self.title}\nContent: {self.content}'
