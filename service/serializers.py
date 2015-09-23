from rest_framework import serializers

from service.models import AutoService

class AutoserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoService
        fields = ('id','logo', 'name','teaser','specialization_work')