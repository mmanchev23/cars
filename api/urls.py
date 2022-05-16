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


def custom_exception_handler(exc, context):
    if isinstance(exc, NotAuthenticated):
        request = context["request"]
        return Response({"You are not logged in!": {
            "register": f"{request.build_absolute_uri()}auth/register/",
            "login": f"{request.build_absolute_uri()}auth/login/",
        }}, status=401)

    return exception_handler(exc, context)


class APIRoot(routers.APIRootView):
    def get_view_name(self) -> str:
        return "Cars"

    def get(self, request):
        if request.user.is_authenticated == True:
            return Response({
                f"Logged in as {request.user.username}": {
                    f"{request.user.username}": f"{request.build_absolute_uri()}user/",
                    "cars": f"{request.build_absolute_uri()}cars/",
                    "docs": f"{request.build_absolute_uri()}docs/",
                    "schema": f"{request.build_absolute_uri()}schema/",
                    "logout": f"{request.build_absolute_uri()}auth/logout/",
                }
            })


class Cars_Router(routers.DefaultRouter):
    APIRootView = APIRoot


API_TITLE = "Cars API"
API_DESCRIPTION = "API for Cars!"
schema_view = get_schema_view(title=API_TITLE)


router = Cars_Router()
router.register(r"user", UserView, "user")
router.register(r"cars", CarView, "cars")


urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/register/", include("dj_rest_auth.registration.urls")),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)), 
    path('schema/', schema_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)