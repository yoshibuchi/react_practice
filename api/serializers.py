from rest_framework import serializers

from SPA.models import Spa


class SpaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spa
        fields = ('title', 'subtitle', 'author', 'isbn')