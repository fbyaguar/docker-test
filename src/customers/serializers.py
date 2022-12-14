from rest_framework import serializers

from src.customers.models import Profile, Technology


class TechnologySerializer(serializers.ModelSerializer):

    class Meta:
        model = Technology
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    technologies = serializers.SlugRelatedField(
        slug_field="name",
        queryset=Technology.objects.all(),
        many=True
    )

    class Meta:
        model = Profile
        fields = '__all__'
