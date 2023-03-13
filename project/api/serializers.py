from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
class bokserializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=bookcreate
        fields=['user','book_name','issue_date']
class bookserializers(serializers.ModelSerializer):
    class Meta:
        model=book
        fields=['bookname']
class ubookserializers(serializers.ModelSerializer):
    class Meta:
        model=ubook
        fields=('__all__')
class issuebookserializers(serializers.ModelSerializer):
    class Meta:
        model=issuebook
        fields=('__all__')

class returnbookserializers(serializers.ModelSerializer):
    class Meta:
        model=returnbook
        fields=('__all__')


    

        
        