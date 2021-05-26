
from .models import reviewModel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviewModel
        fields = ('reviewee_email', 'reviewer_email', 'rating', 'comment', )



class reviewSerializer2(serializers.ModelSerializer):
    class Meta:
        model = reviewModel
        fields = ('reviewee_email', 'reviewer_email', 'rating', 'comment', )