from rest_framework import serializers
from users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ["id","username",'email','ruolo','telefono','fax','first_name','last_name','is_staff']
#        fields = ["username"]
#        fields = '__all__'


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','email','ruolo','telefono','fax','first_name','last_name']
#        fields = '__all__'
