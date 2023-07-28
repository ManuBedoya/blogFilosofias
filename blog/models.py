from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(default="Some")

    def __str__(self):
        return self.title.upper()

    def getDetail(self):
        return f'Title: {self.title}\nContent: {self.content}'

    def getShortContent(self):
        return self.content if len(self.content) < 100 else f'{self.content[:150]}...'

    def getContent(self):
        return self.content

    def isContentShort(self):
        lenCaracteres = len(self.content)
        lenEspacios = self.content.count('\n')
        return True if not (lenEspacios >= 40 or (lenEspacios + lenCaracteres) >= 4930) else False
