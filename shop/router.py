from django.urls import path, include
from shop.api import *


urlpatterns = [
    path('product/all', ProductListApi.as_view(), name='productAll'),
    path('product/<int:pk>', ProductDetailApi.as_view(), name='productDetail'),
    path('category', CategoryListApi.as_view(), name='productAll'),
    path('cart', Cart.as_view(), name='cart'),
    path('product/comment/<int:comment_id>', CommentListApi.as_view(), name='commenList'),
    path('product/comment/create', CommentCreateApi.as_view(), name='commenList'),
    path('order/create', CreateOrder.as_view(), name="orderCreate"),
    path('allSlider', SliderListApi.as_view(), name="getSlider"),
    
]