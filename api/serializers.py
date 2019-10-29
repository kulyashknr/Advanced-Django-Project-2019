from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        # fields = ('size', 'type')
        fields = '__all__'

