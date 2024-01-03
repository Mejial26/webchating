from django.urls import path
from .views import ProfileView, ProfileDetailView

profiles_patterns = ([
    path('profiles/', ProfileView.as_view(), name='perfiles'),
    path('profile/<username>/', ProfileDetailView.as_view(), name='detail'),
    
],'profiles')