from rest_framework import serializers
from .models import Books, Genre, Authors

class BookSerializer(serializers.ModelSerializer):
    Picture = serializers.SerializerMethodField()
    class Meta:
        model = Books
        fields = '__all__'
    
    def get_Picture(self, record: Books):
        return record.Picture.url

