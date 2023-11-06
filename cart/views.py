from django.shortcuts import render, redirect
from bookapp.models import Books
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

# Create your views here.

def _cart_id(request): #this function seeks request the id of the loggedin user and use it as the card id
    if request.user.is_authenticated:
        cart_ID = request.user.id
        return cart_ID

def add_cart(request, book_id):
    book = Books.objects.get(id = book_id) #get the book object that has the same id as the book selected to be added to cart
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))#get the cart object whose cart_id is the same as referenced user_id
    
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request)) #if there isn't any object as such, then create a cart object and assign a cart id(authenticated user_id) to it
        cart.save() #save  cart.

    try:#this applies if there's a book which already exists in the cartItem and the user is adding it again
        cart_item = CartItem.objects.get(book=book, cart=cart) 
        cart_item.quantity +=1 #increase cart quantity by 1 anytime this same book is added to the cart
        cart_item.save()

    except CartItem.DoesNotExist: #this applies if this is the first time this particular book is being added to the CartItem
        cart_item = CartItem.objects.create(book=book, cart=cart, quantity=1) #create a new cart item object with book =selected book object, 
        #equate a cart with cart id and  date added to it and assign quantity=1 to it 
        cart_item.save()
    return redirect('cart:Cart')
#pass all info to the main cart page

def decrease_deactivate(request, book_id):#function to decrement product quantity in cart or delete product from cart 
    cart = Cart.objects.get(cart_id = _cart_id(request))
    book = Books.objects.get(id=book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)

    if cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.is_active = False
        cart_item.save()
    return redirect('cart:Cart')

def remove_cartitem(request, book_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    book  = Books.objects.get(id =book_id)
    cart_item = CartItem.objects.get(book=book, cart=cart)
    cart_item.delete()
    


@api_view(['GET'])
def mycart(request, total=0, quantity = 0, cart_items=None, cart=None ):
    try:
        tax= 0
        Grand_total=0
        cart_items_shown =None
        cart= Cart.objects.get(cart_id=_cart_id(request)) #get the cart with the current user_id
        cart_items = CartItemSerializer(CartItem.objects.filter(cart=cart, is_active = True)).data #go through all car items and select the ones whose id matches the user_id and is active
        cart_items_shown = CartItemSerializer(CartItem.objects.filter(cart=cart)).data#go through all cart items and select the ones whose id matches the user id
        for cart_item in cart_items_shown:
            total += (cart_item.book.Price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = 0.15*total
        Grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore. this function will only run after a cart is created in the name of the user.
    
    context = {
        'total':total, 
        'quantity':quantity, 
        'cart_items_shown': cart_items_shown,
        'tax':tax,
        'Grand_total':Grand_total,
    }
    return Response(context)
