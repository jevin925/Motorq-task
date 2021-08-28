from rest_framework import serializers
from .models import User, user_subject, waiting_list, subjects

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            
            'id':{'read_only': True},

        }

    def create(self, validated_data): 
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjects
        fields = '__all__'
        extra_kwargs = {
            
            'id':{'read_only': True},

        }

    def create(self, validated_data): 
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class UserSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_subject
        fields = '__all__'
        extra_kwargs = {
            
            'id':{'read_only': True},

        }

    def create(self, validated_data): 
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class WaitingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = waiting_list
        fields = '__all__'
        extra_kwargs = {
            
            'id':{'read_only': True},

        }

    def create(self, validated_data): 
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance