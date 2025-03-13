from django.urls import path, include

from auth_service.views import index

urlpatterns = [
    path('auth/', index, name='index'),
    path('auth/social/', include('social_django.urls', namespace='social'))
]