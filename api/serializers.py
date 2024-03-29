from rest_framework import serializers
from .models import MainUser, Company, Vacancy


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

    def validate_salary(self, value):
        if value > 0:
            raise serializers.ValidationError('invalid salary')
        return value
