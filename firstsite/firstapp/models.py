from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    job = models.CharField(null=True, blank=True, max_length=200)

    def __str__(self):
        return self.name

class Aritcle(models.Model):
    headline = models.CharField(null=True,blank=True,max_length=500)
    content = models.TextField(null=True, blank=True)
    #under_comments = XXXXX  相当于在Article表创建了一个under_comments字段
    TAG_CHOICES = (
        ('tech','Tech'),
        ('life','Life'),
        )
    tag = models.CharField(null=True,blank=True,max_length=5,choices=TAG_CHOICES)

    def __str__(self):
        return self.headline

class Comment(models.Model):
    """创建评论模型"""
    name = models.CharField(null=True,blank=True,max_length=50)
    comment = models.TextField(null=True, blank=True)
    belong_to = models.ForeignKey(to=Aritcle, related_name='under_comments',null=True,blank=True)
    best_comment = models.BooleanField(default=False)  #最优评论字段布尔值

    def __str__(self):
        return self.name
