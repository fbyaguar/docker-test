from rest_framework import serializers


class NameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name
