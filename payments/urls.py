from django.urls import path
from . import views

urlpatterns =[
    path('cart/',views.cart_view,name="cart"),
    path('add/<int:article_id>/',views.add_to_cart,name="add_to_cart"),
    path('payment/',views.payment_page,name="payment"),
    path('success/',views.payment_success,name="payment_success"),
    path('increase/<int:cart_id>/',views.increase_quantity,name='increase_quantity'),
    path('decrease/<int:cart_id>/',views.decrease_quantity,name='decrease_quantity'),
    path('remove/<int:cart_id>/',views.remove_item,name='remove_item'),
    path('checkout/',views.checkout_view,name='checkout'),
    path('buy-now/<int:article_id>/',views.buy_now,name="buy_now"),
]