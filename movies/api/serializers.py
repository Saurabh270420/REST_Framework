from rest_framework import serializers
from movies.models import Movies


class MovieSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    active=serializers.BooleanField()
    budget=serializers.IntegerField()

    def create(self,validated_data):
        return Movies.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name')
        instance.active=validated_data.get('active')
        instance.budget=validated_data.get('budget')
        instance.save()
        return instance
        
