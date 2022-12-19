from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Album
import ipdb


class AlbumSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Album
        fields = ["id","user_id", "name", "year"]
        read_only_fields = ["id"]

