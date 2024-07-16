# serializers.py
from rest_framework import serializers
from .models import CustomUser, Patient, Staff, Consultation
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    def create(self, validated_data): 
      validated_data["is_active"] = True
      validated_data["password"] = make_password(validated_data["password"])
      return super().create(validated_data)
      
    class Meta:
      model = CustomUser
      fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        # Field-level validation
        if not attrs.get('username'):
            raise serializers.ValidationError('Username is required.')
        if not attrs.get('password'):
            raise serializers.ValidationError('Password is required.')
        return attrs

class CustomTokenSerializer(serializers.Serializer):
  token = serializers.CharField(source='key')
  user = UserSerializer()
  
class PatientSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  
  class Meta: 
    model = Patient
    fields = "__all__"
    
class StaffSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  
  class Meta: 
    model = Staff
    fields = "__all__"
    
class ConsultationSerializer(serializers.ModelSerializer):
  staff = StaffSerializer(many=True)
  patient = PatientSerializer()
  
  class Meta: 
    model = Consultation
    fields = "__all__"