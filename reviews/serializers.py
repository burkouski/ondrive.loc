from rest_framework import serializers
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):


    class Meta:
        model = Review
        fields = ('author', 'pub_date', 'review', 'rate','content_type', 'object_id')

