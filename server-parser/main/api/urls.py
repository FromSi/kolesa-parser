from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', views.UserCreateAPIView.as_view()),
    path('email/', views.email_profile),
    path('ads/', views.get_user_ads),
    path('clear/ads/', views.clear_all_ads),
    path('auth/', obtain_auth_token),
    path('filter/', views.update_filter),
]
