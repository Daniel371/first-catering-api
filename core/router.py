
from .views import ProfileViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', ProfileViewSet, basename='profile')
