from .views import *
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.schemas import get_schema_view
from rest_framework.exceptions import NotAuthenticated
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r"users", UserView, "users")
router.register(r"brands", CarBrandView, "car_brands")
router.register(r"models", CarModelView, "car_models")
router.register(r"user-car", UserCarView, "user_car")
router.register(r"cars", CarView, "cars")


urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)