from django.shortcuts import get_object_or_404, get_list_or_404

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

    def get(self, request, category_name):
        foods = models.Food.objects.filter(category__name_uz=category_name)
        serializer = serializers.FoodListSerializer(foods, many=True)

        return Response(serializer.data)

class FoodApiView(APIView):
    def get(self, request, food_name):
        food = get_object_or_404(models.Food, name_uz=food_name)
        serializer = serializers.FoodSerializer(food)

        return Response(serializer.data)
