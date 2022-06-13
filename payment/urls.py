from django.urls import include, path
from django.conf.urls import url
from .views import PaymentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'', PaymentViewSet, basename='payment')

urlpatterns = []
urlpatterns += router.urls