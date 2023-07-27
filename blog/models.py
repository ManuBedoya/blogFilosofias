from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default="Some")

    def __str__(self):
        return self.title

    def getDetail(self):
        return f'Title: {self.title}\nContent: {self.content}'

    def getShortContent(self):
        return self.content if len(self.content) < 100 else f'{self.content[:250]}...'
