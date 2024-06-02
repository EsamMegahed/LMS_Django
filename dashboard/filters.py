import django_filters 
from django.contrib.auth.models import User


class UsersFilter(django_filters.FilterSet):

    username = django_filters.CharFilter(lookup_expr='icontains',label='')
    class Meta:
        model = User
        fields = ['username']
        # fields = {'username':['icontains'],
        #           'email':['icontains']
        #           }

