from rest_framework import serializers
from reviews.models import ReviewsModel


class ReviewsSerializers(serializers.ModelSerializer):

    class Meta:

        model = ReviewsModel
        fields = ('name', 'date', 'text')
