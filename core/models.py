import datetime
from django.db import models
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    article_number = models.IntegerField()

    def __str__(self):
        return self.category_name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    writer_name = models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.tittle

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
#
#
# # class Writer(models.Model):
# #     article = models.ForeignKey(Article, on_delete=models.CASCADE)
# #     tittle = models.CharField(max_length=200)
# #     name = models.CharField()
# #     email = models.CharField()
# #     article_number = models.IntegerField()
#
