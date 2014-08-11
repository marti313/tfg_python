# -*- coding: utf-8 -*-
from rest_framework import serializers
from models import Keyword, Subject, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject

class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword