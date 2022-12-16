from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import CreateAPIView, ListAPIView



class SongView(CreateAPIView, ListAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        return self.queryset.filter(album_id=self.kwargs['pk'])
    def perform_create(self, serializer):
        album = Album.objects.get(id= self.kwargs['pk'])
        serializer.save(album=album)
