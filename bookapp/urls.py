from django.urls import path 

from . import views


app_name = 'bookapp'

urlpatterns =[
    path('addbook/', views.BookRegistration, name = 'add_book'), 
    path('home/',views.GeneralHomePage, name = 'home'), #(url for general homepage irrespective of the store owner)
    path('home/<slug:genre_slug>/', views.GeneralHomePage, name='book_by_genre'), #(url for general homepage to view books based on the genre or category)
   #path('authorlist/', Authorlist.as_view(template_name = 'bookapp/authorlist.html'), name = 'authorlist'),   
    #path('authordetail/<int:pk>/', Authordetail.as_view(template_name = 'authordetail.html'), name='authordetail'),  
    path('<slug:genre_slug>/<slug:book_slug>/', views.book_detail, name='bookdetail'),
    path('search/', views.search_book, name = 'search'),
    #path('<slug:store_slug>/<slug:genre_slug>/<slug:book_slug>/', views.book_detail, name='bookdetail_store_category'),
    #path('<slug:book_slug>/', views.book_detail, name='bookdetail_from_homepage'),
]