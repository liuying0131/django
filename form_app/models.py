#coding:utf-8
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('姓名',max_length=50)
    password = models.CharField(max_length=50)


    def __unicode__(self):
        return self.username
SEX_CHOICES = (
    ('0','男'),
    ('1','女'),
)
UserWork_CHOICES = (
    ('0','学生'),
    ('1','老师'),
)

class Student(models.Model):
    acaname=models.CharField('学_院',max_length=50,null=True)
    classnum=models.CharField('班_级',max_length=50,null=True)
    stuid=models.CharField('学_号',max_length=50,null=True)
    username=models.CharField('姓_名',max_length=50,null=True)
    sex = models.CharField('性_别',choices = SEX_CHOICES,max_length = 1,null=True)

class Grade(models.Model):
    acaname=models.CharField('学_院',max_length=50)
    stuid=models.CharField('学_号',max_length=50)
    username=models.CharField('姓_名',max_length=50)
    grade1=models.IntegerField('英_语',null=True)
    grade2 = models.IntegerField('高_数',null=True)
    grade3=models.IntegerField('大_物',null=True)

class Review(models.Model):
    student=models.IntegerField("学号")
    index1=models.IntegerField("思想品德")
    index2=models.IntegerField("学习成绩")
    index3=models.IntegerField("身体素质")
    index4=models.IntegerField("组织能力")

    def __unicode__(self):
        return self.student
