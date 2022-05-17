from .views import *
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated
from rest_framework.documentation import include_docs_urls
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
      title="Cars API",
      default_version='v1',
      description="API for Cars",
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)


def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        request = context["request"]
        return Response({"You are not logged in!": {
            "register": f"{request.build_absolute_uri()}auth/register/",
            "login": f"{request.build_absolute_uri()}auth/login/",
            "admin": f"{request.build_absolute_uri()}admin/",
        }}, status=401)

    return exception_handler(exc, context)


class APIRoot(routers.APIRootView):
    def get_view_name(self) -> str:
        return "Cars"

    def get(self, request):
        if request.user.is_authenticated == True:
            return Response({
                f"Logged in as {request.user.username}": {
                    "users": f"{request.build_absolute_uri()}users/",
                    "brands": f"{request.build_absolute_uri()}brands/",
                    "models": f"{request.build_absolute_uri()}models/",
                    "user-car": f"{request.build_absolute_uri()}user-car/",
                    "cars": f"{request.build_absolute_uri()}cars/",
                    "admin": f"{request.build_absolute_uri()}admin/",
                    "schema": f"{request.build_absolute_uri()}swagger/",
                    "logout": f"{request.build_absolute_uri()}auth/logout/",
                }
            })


class Cars_Router(routers.DefaultRouter):
    APIRootView = APIRoot


API_TITLE = "Cars API"
API_DESCRIPTION = "API for Cars!"

router = Cars_Router()
router.register(r"users", UserView, "users")
router.register(r"brands", CarBrandView, "car_brands")
router.register(r"models", CarModelView, "car_models")
router.register(r"user-car", UserCarView, "user_car")
router.register(r"cars", CarView, "cars")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", include("dj_rest_auth.registration.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)