from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView

from . import serializers
from . import models

# Create your views here.

class CategoryListApiView(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.all()

class FoodsListApiView(APIView):

    def get(self, request, category_id):
        foods = models.Food.objects.filter(category__id=category_id)
        serializer = serializers.FoodListSerializer(foods, many=True)

        return Response(serializer.data)

class FoodsApiView(generics.RetrieveAPIView):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer