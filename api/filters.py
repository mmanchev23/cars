from django_filters import rest_framework as filters
from .models import *

class UserFilter(filters.FilterSet):
    username = filters.CharFilter(lookup_expr="iexact")
    first_name = filters.CharFilter(lookup_expr="iexact")
    last_name = filters.CharFilter(lookup_expr="iexact")
    email = filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
