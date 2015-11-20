from django.contrib.auth.models import User, Group
from rest_framework import serializers
from models import *
# from models import Musician, Album

class UserSerializer(serializers.ModelSerializer):
    # city = serializers.CharField(source='myuser.city')
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name','groups')
        write_only_fields = ('password',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
            

        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Group
        fields = ('url', 'name')


class FollowingSerializer(serializers.HyperlinkedModelSerializer):
    # username = serializers.CharField(source='User.username', read_only=True)
    class Meta:
        model = Following
        fields = ('follower',)

# class MusicianSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Musician
#         fields = ('id','first_name','last_name','instrumnet')
        

# class AlbumSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Album
#         fields = ('url','artist','name','release_date')
