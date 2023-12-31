from rest_framework import serializers

from .models import Category, Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "isbn",
            "title",
            "author",
            "description",
            "slug",
            "date_added",
            "category",
            "available",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "books",
        )