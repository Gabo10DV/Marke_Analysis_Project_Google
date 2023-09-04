from rest_framework import routers
from .api import PlaceViewSet

router = routers.DefaultRouter()

router.register('api/Place',PlaceViewSet,'places')

urlpatterns=router.urls