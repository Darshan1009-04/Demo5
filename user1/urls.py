from django.urls import path
from .views import user_list

urlpatterns = [
    path('user1/', user_list),
]