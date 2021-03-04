
from django.urls import path, include
from .views import findProfile
from .router import router


urlpatterns = [
    path('', include(router.urls)),
    path('find/', findProfile, name='test'),
]
