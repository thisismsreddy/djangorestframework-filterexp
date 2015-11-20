from django.contrib.auth.models import User, Group 
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from quickstart.serializers import UserSerializer, GroupSerializer, FollowingSerializer
from rest_framework.views import APIView
from rest_framework import filters
from quickstart.models import *

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('username', 'email', 'id')


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MyView(APIView):

    def get(self, request, *arga, **kwargs):
        e_profiles = Following.objects.filter(followee__pk=request.GET.get('followee_id'))

        # Then call you serializer

        e_serialized = FollowingSerializer(e_profiles, context={'request': request} , many=True)
        return Response(e_serialized.data )    

# class MusicianViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Musician.objects.all()
#     serializer_class = MusicianSerializer
    
    
    

# class AlbumViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Album.objects.all()
#     serializer_class = AlbumSerializer    