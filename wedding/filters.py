import django_filters
from wedding.models import Guest
from wedding.forms import SearchForm

class GuestFilter(django_filters.FilterSet):
    class Meta:
        model = Guest
        fields = ['fullName','email']
        form = SearchForm
