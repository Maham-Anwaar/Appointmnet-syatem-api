
from rest_framework import serializers
from users import models


class DoctorSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.Doctor
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
        
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.Doctor.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
    
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Appointment
        fields = ('p_id', 'd_id')
        
    # def create(self, validated_data):
    #     """Create and return a new appoinement"""
    #     apt = models.Appointment()
        
    #     apt.createAppointment(
    #         p_id=validated_data['p_id'],
    #         d_id=validated_data['d_id'],
    #     )

    #     return apt

    # def update(self, instance, validated_data):
    #     """Handle updating user app"""
    #     return super().update(instance, validated_data)

class AppointmnetDetailsSerializer(serializers.ModelSerializer):
    pat_name = serializers.CharField(source='p_id', read_only=True)

    class Meta:
        model = models.Appointment
        fields = ('d_id', 'p_id','pat_name' )

class AppointmnetDetailsSerializer (serializers.ModelSerializer):
    p_name = serializers.CharField(source='p_id.name', read_only=True)

    class Meta:
        model = models.Appointment
        fields = ('p_name', 'p_id', 'd_id')