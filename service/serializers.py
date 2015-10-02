from rest_framework import serializers

from service.models import AutoService, CarWash, TireService

class AutoserviceSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    class Meta:
        model = AutoService
        fields = ('id','url','logo', 'name','teaser','city','address','building' ,'specialization_work',
                  'repair_work','diag_work','serv_work','add_work','add_services',
                  'longitude','latitude')

    def get_url(self, obj):
        return obj.get_absolute_url()


class CarWashSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarWash
        fields = ('id','logo', 'name','teaser','city','address','building' ,'type_carwash',
                  'type_vehicle','car_wash_services','add_services')


class TireServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TireService
        fields = ('id','logo', 'name','teaser','city','address','building' ,'tire_work',
                  'disc_work','add_services')