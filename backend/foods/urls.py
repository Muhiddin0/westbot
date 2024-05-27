from django.urls import path

from . import views 

urlpatterns = [
    path('/food/category/', views.CategoryListApiView.as_view()),
    path('/food/category/<int:category_id>/', views.FoodsListApiView.as_view()),
    path('foods/<int:category_id>/', views.FoodsApiView.as_view()),
]
