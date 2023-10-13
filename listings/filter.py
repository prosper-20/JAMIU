from django_filters.rest_framework import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        models = Property
        fields = "__all__"