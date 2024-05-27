from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard),

    path('bot/users/', views.GetBotUsers.as_view()),
    path('bot/users/<int:user_id>', views.GetBotUser.as_view()),

    path('busket/list', views.GetUserBasketItems),
    path('busket/item', views.ChangeBasketItem),
    path('busket/change', views.ChangeBasketItem),
    path('busket/clear-and-rating', views.ClearUserBasketAndSetRating),
    path('busket/delete', views.DeleteBasket),
]