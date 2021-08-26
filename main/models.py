from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.CharField(max_length=500)
    qtype = models.CharField(max_length=50)
    answer = models.CharField(max_length=500)
    answer1 = models.CharField(max_length=500)
    answer2 = models.CharField(max_length=500)
    answer3 = models.CharField(max_length=500)
    img = models.FileField(default="/assets/logo.png")
    img1 = models.FileField(default="/assets/logo.png")
    img2 = models.FileField(default="/assets/logo.png")
    img3 = models.FileField(default="/assets/logo.png")


class Test(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.BigIntegerField()
    question = models.CharField(max_length=500)
    qtype = models.CharField(max_length=50)
    mt_s = models.CharField(max_length=500, default="None")
    mt_a = models.CharField(max_length=500, default="None")
    mc_s = models.CharField(max_length=500, default="None")
    mc_a = models.CharField(max_length=500, default="None")
    fb_s = models.CharField(max_length=500, default="None")
    fb_a = models.CharField(max_length=500, default="None")
    tf_s = models.CharField(max_length=500, default="None")
    tf_a = models.CharField(max_length=500, default="None")


class Key(models.Model):
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=100)


class Grades(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)
    grade = models.IntegerField()
