from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

        def validate_title(self, value):
            if len(value.strip()) < 3:
                raise serializers.ValidationError(
                    "Title must contain atleast 3 characters"
                )

            return value

        def validate_due_date(self, value):
            from datetime import date

            if value < date.today():
                raise serializers.ValidationError("Due date cannot be in the past.")
            return value
