from rest_framework import serializers

from service.models import AutoService, CarWash, TireService


class AutoserviceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = AutoService
        fields = ('id', 'url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude',
                  'specialization_work',
                  'repair_work', 'diag_work', 'serv_work', 'add_work', 'add_services')

    def get_url(self, obj):
        return obj.get_absolute_url()


class CarWashSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = CarWash
        fields = (
        'id','url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude', 'type_carwash',
        'type_vehicle', 'car_wash_services', 'add_services')
    def get_url(self, obj):
        return obj.get_absolute_url()


class TireServiceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = TireService
        fields = ('id','url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude', 'tire_work',
                  'disc_work', 'add_services')

    def get_url(self, obj):
        return obj.get_absolute_url()