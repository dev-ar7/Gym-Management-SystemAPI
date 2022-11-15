from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'password', 'phone',
                  'gender', 'is_active', 'is_staff', 'is_superuser']
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.times():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class EnquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'contactNO', 'emailID', 'age',
                    'gender', 'context']


class EquipmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment
        fields = ['id', 'name', 'price', 'unit', 'date', 'desc']


class PlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plan
        fields = ['id', 'name', 'desc', 'price', 'duration']


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ['id', 'name', 'contactNo', 'emailId',
                    'age', 'gender', 'plan', 'joinDate', 'expDate',
                    'totalAmount', 'initialAmount', 'dueAmount']

