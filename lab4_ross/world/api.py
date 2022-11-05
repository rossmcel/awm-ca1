from rest_framework import routers

# from viewsets import WorldBorderViewSet
from . import viewsets

router = routers.DefaultRouter()
router.register(r"WorldBorder", viewsets.WorldBorderViewSet)

urlpatterns = router.urls
