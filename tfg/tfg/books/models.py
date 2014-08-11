# -*- coding: utf-8 -*-
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=9000)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    isbn = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    subject = models.ForeignKey(Subject)


    def __unicode__(self):
        return self.title


class Keyword(models.Model):
    key = models.CharField(max_length=15)
    value = models.CharField(max_length=9000, blank=True, null= True)

