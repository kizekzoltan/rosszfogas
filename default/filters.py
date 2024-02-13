import django_filters
from django_filters import CharFilter
from .models import *

class ProductFilter(django_filters.FilterSet):
    namecat = django_filters.CharFilter(method='filter_by_name_or_category', label='Search by Name or Category')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Minimum Price')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Maximum Price')

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['customer', 'description', 'feladocim', 'terms_checkbox', 'image']

    def filter_by_name_or_category(self, queryset, name, value):
        return queryset.filter(
            models.Q(name__icontains=value) |
            models.Q(kategoria__icontains=value)
        )