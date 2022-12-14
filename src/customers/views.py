from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from customers.filters import TechnologiesFilter
from customers.pagination import CustomersPagination
from customers.permissions import IsArdminOrReadOnly, IsAuthorOrAdmin
from src.customers.models import Profile, Technology
from src.customers.serializers import ProfileSerializer, TechnologySerializer


class ProfileModelViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().filter(user__is_active=True).order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdmin)
    pagination_class = CustomersPagination
    filterset_class = TechnologiesFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TechnologyModelViewSet(viewsets.ModelViewSet):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = (IsArdminOrReadOnly,)
