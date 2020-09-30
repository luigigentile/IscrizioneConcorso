from django.urls import include,path

from users.api.views import CurrentUserAPIView
from users.api.views import UsersAPIView

from users.api.views import UserRUDAPIView


from rest_framework.routers import DefaultRouter
from users.api.views import UsersViewSet

router = DefaultRouter()
router.register(r"usersviewset",UsersViewSet)


urlpatterns = [
    path('user/', CurrentUserAPIView.as_view(), name = 'current-user'),
    path('users/', UsersAPIView.as_view(), name = 'users'),
    path('user/<int:pk>/', UserRUDAPIView.as_view(), name = 'current-user-update'),
    path('', include(router.urls))


]
