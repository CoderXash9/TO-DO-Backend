from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("LOW", "low"),
        ("MEDIUM", "medium"),
        ("HIGH", "high"),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="MEDIUM",
    )

    due_date = models.DateField(
        null=True,
        blank=True,
        
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
