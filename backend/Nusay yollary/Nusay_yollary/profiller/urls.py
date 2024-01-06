from django.urls import path
from rest_framework import routers
from .views import ProfillerList

router = routers.DefaultRouter()

router.register('profile', ProfillerList)

urlpatterns = router.urls
