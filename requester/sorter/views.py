import os
import random
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Selection
from .serializers import SelectionSerializer

class ImageViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['get'])
    def get_images(self, request):
        """Fetch 10 random images from the media folder"""
        image_folder = os.path.join(settings.MEDIA_ROOT, "images")
        all_images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

        if not all_images:
            return Response({"error": "No images found"}, status=404)

        selected_images = random.sample(all_images, min(10, len(all_images)))  # Select up to 10 images

        return Response({"images": [f"{settings.MEDIA_URL}images/{img}" for img in selected_images]})

    @action(detail=False, methods=['post'])
    def submit_label(self, request):
        """Store user selection and generate a token every 10 labels"""
        image_name = request.data.get("image_name")
        label = request.data.get("label")

        if not image_name or not label:
            return Response({"error": "Invalid data"}, status=400)

        Selection.objects.create(image_name=image_name, label=label)

        # Count total selections
        selection_count = Selection.objects.count()
        token = None
        if selection_count % 10 == 0:
            token = f"TOKEN_{random.randint(1000, 9999)}"  # Generate a token

        return Response({"message": "Label submitted!", "token": token})
