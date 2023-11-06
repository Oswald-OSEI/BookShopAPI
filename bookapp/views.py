from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Books, Genre, Authors
from users.models import CustomUser
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import BookForm, AuthorsForm, GenreForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from rest_framework.decorators import api_view, parser_classes
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

# Create your views here.
@api_view(['POST'])
def BookRegistration(request):
    
    #initial = {'Uploader':request.user}
    #BookForm(initial=initial)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data) #(get the posted json data and deserialize it into a format the database can save)
        
        if serializer.is_valid(raise_exception = True): #if it's not valid, return the error
            serializer.save() #save the instance into the database
        return  Response(serializer.data) #(return json response of the saved data)
    #else:
     #   form = BookForm()
      #  context = {'form':form}
       # return render(request, 'bookapp/add_book.html', context)

#The general homepage contains all  books irrespective of which store it belongs to.

@api_view(['GET'])
def GeneralHomePage(request, genre_slug=None):
    genre = None
    books = None
    #set books, genre and genre_slug to none.
    if genre_slug != None: #if the user enters a particular slug,then the genre slug isn't none so this statement will run
        genre = get_object_or_404(Genre, slug=genre_slug) #get the genre object whose slug is equal to the inputted slug
        books = Books.objects.all().filter(Genre=genre, is_available=True) #get all available book objects whose genre equal to the previous defined genre
        books_count = books.count()
        Bookdata = BookSerializer(books, many=True).data #(translate python instance into native data types and get the data)

    else: #if the user doesn't enter any genre_slug, then the genre_slug is none and all available books irrespective of genre shows
        books = Books.objects.all().filter(is_available=True)
        books_count = books.count()
        Bookdata = BookSerializer(books, many=True).data #(translate python instance into native data types and get the data)
   
    context = {
        'Bookdata': Bookdata, 
        'books_count':books_count,
    }
    return Response(context) #(render the json response to the user)

@api_view(['GET'])    
def book_detail(request, genre_slug=None, book_slug=None): #store_slug=None):
    try:
        #check if url contains genre_slug
        #double underscore picks the slug of the genre mapped to the object. this is then mapped to the genre slug from the url
        #the book slug from the url is subsequently mapped to the slug of the particular book object
        single_book_detail = Books.objects.get(Genre__slug=genre_slug, slug = book_slug)
        book_details = BookSerializer(single_book_detail).data

    except Exception as e:
        raise e
    context = {
        'book_details':book_details,

    }
    return Response(context)

@api_view(['GET'])
def search_book(request):
    if 'keyword' in request.GET: #recieve keyword from form
       keyword = request.GET['keyword'] #receive keyword and store it in the variable
       if keyword: #check if keyword isn't none
            books = Books.objects.all().order_by('Title').filter(Title__icontains=keyword)
            searched_book = BookSerializer(books).data

    context = {
        'searched_book':searched_book
    }
    return Response(context)
