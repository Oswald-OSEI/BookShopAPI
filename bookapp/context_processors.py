from .models import Genre

#this takes a request as an argument and returns dictionay of data as a context

def menu_links(request):
    link = Genre.objects.all() #make a request for all genre objects in the database 
    return dict(link=link)

    