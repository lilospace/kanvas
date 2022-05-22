from rest_framework.urls import urlpatterns, path
from .views import CreateUser

urlpatterns = [
    path('register/', CreateUser.as_view())
]