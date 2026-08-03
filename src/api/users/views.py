from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status, views, generics
from rest_framework.response import Response
from users.serializers import ResponseSerializer
# Create your views here.
def profile_view(request):
    data = {
        'id': '1',
        'name': 'Ayo',
        'gender': 'male'
    }
    return JsonResponse(data)

class ResponseClass(generics.GenericAPIView):
    serializer_class = ResponseSerializer
    def get(self, request):
        payload_data = {
            "ID": "AIESEC12",
            "Name": "Ademola Oluwashola",
            "Gender": "Male",
            "Department": "Computer Engineering",
        }
        return Response(payload_data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"message": "OK"}, status=status.HTTP_201_CREATED)

# class