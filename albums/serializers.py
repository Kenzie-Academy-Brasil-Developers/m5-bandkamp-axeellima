from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Album
import ipdb


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Album
        fields = "__all__"
        extra_kwargs = {'user': {'write_only': True}}

