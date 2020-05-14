# https://www.django-rest-framework.org/api-guide/serializers/

from rest_framework import serializers

from meetings.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('date', 'startTime', 'endTime', 'title', 'description', 'people')
