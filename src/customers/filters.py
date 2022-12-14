from django_filters import FilterSet, AllValuesFilter

from src.customers.models import Profile


class TechnologiesFilter(FilterSet):
    technologies_name = AllValuesFilter(field_name='technologies__name')

    class Meta:
        model = Profile
        fields = ('technologies_name',)
