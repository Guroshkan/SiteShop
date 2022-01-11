from django.urls import path
from .views import ProductView, PriceView, TypeView

app_name = "Shop"

urlpatterns = [
    path('product/', ProductView.as_view()),
    path('price/', PriceView.as_view()),
    path('type/', TypeView.as_view()),
    path('product/<int:pk>', ProductView.as_view()),
    path('price/<int:pk>', PriceView.as_view()),
    path('type/<int:pk>', TypeView.as_view())
]