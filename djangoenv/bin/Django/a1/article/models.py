from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = "article"
    article_tittle = models.CharField(max_length=200)
    article_date = models.DateTimeField()
    article_text = models.TextField()
    article_likes = models.IntegerField(default=0)

class Commets(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField()
    comments_article = models.ForeignKey(Article)
