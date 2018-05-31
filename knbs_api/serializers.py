from rest_framework import serializers
from .models import Counties


class CountiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Counties
        #fields = ('county_id', 'county_name')
        fields = '__all__'


