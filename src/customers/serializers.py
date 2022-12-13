from rest_framework import serializers

from src.customers.fields import NameField
from src.customers.models import Profile, Technology


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    technologies = NameField(many=True, queryset=Technology.objects.all())

    class Meta:
        model = Profile
        fields = '__all__'
