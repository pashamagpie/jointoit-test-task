import django_filters

from .models import Event


class EventFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')
    organizer = django_filters.CharFilter(field_name='organizer__username', lookup_expr='icontains')
    date_after = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_before = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['title', 'location', 'organizer', 'date_after', 'date_before']
