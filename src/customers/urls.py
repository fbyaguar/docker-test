from django.urls import path, include
from rest_framework.routers import SimpleRouter

from src.customers.views import ProfileModelViewSet, TechnologyModelViewSet

router = SimpleRouter()
router.register(r'profile', ProfileModelViewSet)

router2 = SimpleRouter()
router2.register(r'technology', TechnologyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(router2.urls))
]
