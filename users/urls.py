from django.urls import path

from .views import UserIndexView

app_name = "users"
urlpatterns = [
    path('profile/<int:pk>/', UserIndexView.as_view(), name='user_profile'),

]
