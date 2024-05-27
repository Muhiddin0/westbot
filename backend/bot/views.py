from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import serializers
from foods.models import Food

from bot.models import User, Basket

# Create your views here.

class GetBotUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.GetBotUserSerializer


class GetBotUser(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, user_id=user_id)
        serializer = serializers.GetBotUserSerializer(user)
        return Response(serializer.data)
    

@api_view(['GET'])
def GetUserBasketItems(request):
    # get query params
    user_id = request.GET.get('user_id')

    if not user_id:
        return Response({
            'status': 'error',
            'message': 'user_id and food_id is required'
        }, status=400)

    basket = get_list_or_404(Basket, user__user_id=user_id)
    serializer = serializers.BasketSerializer(basket, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def GetUserBasketItem(request):
    # get query params
    basket_id = request.GET.get('basket_id')

    if not basket_id:
        return Response({
            'status': 'error',
            'message': 'user_id and food_id is required'
        }, status=400)

    basket = get_object_or_404(Basket, pk=basket_id)

    if request.method == 'GET':
        serializer = serializers.BasketSerializer(basket)
        return Response(serializer.data)


@api_view(['GET'])
def ChangeBasketItem(request):
    basket_id = request.GET.get('basket_id')
    action = request.GET.get('action')

    basket = get_object_or_404(Basket, pk=basket_id)

    if request.method == 'GET':
        if action == "incr":
            basket.count = basket.count + 1
        if action == "decr":
            basket.count = basket.count - 1
        basket.save()
        serializer = serializers.BasketSerializer(basket)
        return Response(serializer.data)


@api_view(['GET'])
def ClearUserBasketAndSetRating(request):
    user_id = request.GET.get('user_id')

    if not user_id:
        return Response({
            "status": False,
            "user_id": "user_id is required"
        })

    basket = Basket.objects.filter(user__user_id=user_id)

    for i in basket:
        food_id = i.food.pk
        food = Food.objects.get(pk=food_id)
        food.shop_rating += i.count
        food.save()

    basket.delete()

    return Response({
        "status": True,
        "message": "Basket succes delete"
    })


@api_view(['GET'])
def DeleteBasket(request):
    basket_id = request.GET.get('basket_id')

    if not basket_id:
        return Response({
            "status": False,
            "basket_id": "basket_id is required"
        })

    basket = Basket.objects.get(id=basket_id)

    basket.delete()

    return Response({
        "status": True,
        "message": "Basket succes delete"
    })


# Admin Views
def dashboard(request):
    return render(request, 'admin/dashboard.html')