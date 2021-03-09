from rest_framework.response  import Response
from rest_framework.views import APIView
from users.models import CustomUser
from users.api.serializers import  UserDisplaySerializer,UserUpdateSerializer
from rest_framework import generics

from rest_framework.permissions import  IsAuthenticated,IsAdminUser
#from questions.api.permissions import IsAuthorOrReadOnly
from users.api.permissions import IsOwnProfileOrReadOnly


#   Prove di viewset e filter
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet


class CurrentUserAPIView(APIView):
    def get(self,request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

class UsersAPIView(generics.ListAPIView):
    queryset=CustomUser.objects.all().order_by("id")
    serializer_class =  UserDisplaySerializer
#    permission_classes = [IsAuthenticated]


class UserRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=CustomUser.objects.all()
    serializer_class =  UserUpdateSerializer
    permission_classes = [IsAuthenticated,IsOwnProfileOrReadOnly]

class UsersViewSet(ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class =  UserUpdateSerializer
    permission_classes = [IsAuthenticated]
#    permission_classes = [IsAuthenticated,IsOwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["first_name"]
    ordering_fields = ['id']

