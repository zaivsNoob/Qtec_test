import django_filters
from .models import Product
from django.forms.widgets import RadioSelect
from .utility import warranty_choices,category_choices

class ProductFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(field_name='price', label='Price from', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', label='to', lookup_expr='lte')
    warranty = django_filters.ChoiceFilter(choices=warranty_choices, empty_label='All Warranties', widget=RadioSelect)
    category = django_filters.ChoiceFilter(choices=category_choices, empty_label='All Categories', widget=RadioSelect)


    class Meta:

        model = Product
        fields = {
            'warranty': ['exact'],
            'category': ['exact'],
          
        }

       

