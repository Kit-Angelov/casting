from django_filters import FilterSet
from django_filters import filters
from . import models
import rest_framework_filters as filters2


class Employee_by_name_Filter(FilterSet):
    """
    TEXT FILTER
    """
    username = filters2.CharFilter(field_name='username')

    class Meta:
        model = models.Employee
        fields = {'username': ['exact', 'startswith']}


class F(FilterSet):
    """
    BOOL FILTER
    """
    """Filter for Books by if books are published or not"""
    check_params = filters.BooleanFilter(name='check_params') #, method='params_checked')
    username = filters2.CharFilter(field_name='username')

    # def params_checked(self, queryset, name, value):
    #     # construct the full lookup expression.
    #     lookup = '__'.join([name, 'isnull'])
    #     return queryset.filter(**{lookup: False})

        # # alternatively, it may not be necessary to construct the lookup.
        # return queryset.filter(published_on__isnull=False)

    class Meta:
        model = models.Employee
        fields = ['check_params', 'username']


# class Author_by_paper_title_Filter(filters.FilterSet):
#     title = filters.AllLookupsFilter()
#     author__name = filters.CharFilter(field_name='author__name', lookup_expr='startswith')
#
#     class Meta:
#         model = models.Paper
#         fields = []