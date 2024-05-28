from django.urls import path

from . import views 

urlpatterns = [
    path('foods/category/', views.CategoryListApiView.as_view()),
    path('foods/category/<int:category_id>/', views.FoodsListApiView.as_view()),
    path('foods/<int:category_id>/', views.FoodsApiView.as_view()),
]
