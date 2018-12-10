from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    article_number = models.IntegerField()


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tittle = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    writer_name = models.IntegerField(default=0)
    category_name = models.CharField(max_length=200)
#
#
# # class Writer(models.Model):
# #     article = models.ForeignKey(Article, on_delete=models.CASCADE)
# #     tittle = models.CharField(max_length=200)
# #     name = models.CharField()
# #     email = models.CharField()
# #     article_number = models.IntegerField()
#
