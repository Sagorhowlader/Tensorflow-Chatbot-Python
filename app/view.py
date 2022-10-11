from rest_framework.views import APIView
from django.http import JsonResponse

from app.training import training_model


class TrainingModel(APIView):
    def post(self, request):
        training_model()
        return JsonResponse({'status': 200})
