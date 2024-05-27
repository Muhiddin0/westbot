from rest_framework.serializers import ModelSerializer

from .models import User, Basket

class GetBotUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id', 'count', 'food', )
        depth = 2