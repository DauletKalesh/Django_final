from rest_framework import serializers
from main.models import Book, Journal

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        exclude = ('id',)

class JournalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        exclude = ('id',)