from django.urls import path
from . import views 
app_name="cart"

urlpatterns=[
    path('mycart/', views.mycart, name = 'Cart'),
    path('add_cart/<int:book_id>/', views.add_cart, name = 'addcart'),
    path('decrease or delete/<int:book_id>', views.decrease_deactivate, name = 'decrease/delete'),
    path('removeitem/<int:book_id>', views.remove_cartitem, name = 'remove_cartitem'),
]