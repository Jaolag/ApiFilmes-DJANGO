from django.urls import path
from . import views

from api.views import ListCreateFilme, DetailUpdateDeleteFilme, UserSignup
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatters = [
    # API Filmes4
 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserSignup.as_view()),
    path('filmes', ListCreateFilme.as_view(), name='list-create-filme'),
    path('filmes/<int:pk>', DetailUpdateDeleteFilme.as_view(),
         name='detail-update-delete-filme')
]


