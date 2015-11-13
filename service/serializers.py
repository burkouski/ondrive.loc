from rest_framework import serializers
from service.models import AutoService, CarWash, TireService


class AutoserviceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = AutoService
        fields = ('id', 'url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude','rating',
                  'specialization_work',
                  'repair_work', 'diag_work', 'serv_work', 'add_work', 'add_services')

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_rating(self, obj):
        return obj.get_rating()


class CarWashSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = CarWash
        fields = (
        'id','url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude', 'rating',
        'type_carwash','type_vehicle', 'carwash_services', 'add_services')

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_rating(self, obj):
        return obj.get_rating()


class TireServiceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = TireService
        fields = ('id','url', 'logo', 'name', 'teaser', 'city', 'address', 'building', 'longitude', 'latitude', 'tire_work','rating',
                  'disc_work', 'add_services')

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_rating(self, obj):
        return obj.get_rating()