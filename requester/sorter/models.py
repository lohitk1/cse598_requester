from django.db import models

class Selection(models.Model):
    image_name = models.CharField(max_length=255)  # Stores filename, not actual image
    label = models.CharField(max_length=10, choices=[("AI", "AI"), ("Real", "Real")])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.image_name} - {self.label}"
