from django.db import models
from django.conf import settings 
from users.models import CustomUser
from django.urls import reverse


# Create your models here.



class Authors(models.Model):
    first_name = models.CharField(max_length = 100, null = True)
    last_name = models.CharField(max_length = 100, null= True)
    slug = models.SlugField(max_length = 100, unique = True, null=True)
    Picture = models.ImageField(upload_to = 'images/authors/Pictures', null=True)
    about_author = models.TextField(null = True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return f'{self.first_name}'
        
class Genre(models.Model):
    genre = models.CharField(max_length = 100, null = True)
    slug = models.SlugField(max_length = 100, unique = True, null=True)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    def get_url(self):
        return reverse('bookcategory', args = [self.slug])

    
    def __str__(self):
        return self.genre
    
class Books(models.Model):
    Title = models.CharField(max_length =100)
    author = models.ForeignKey(Authors, null = True, on_delete=models.SET_NULL)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, on_delete=models.SET_NULL)
    Genre = models.ForeignKey(Genre, null = True, on_delete=models.SET_NULL)
    edition = models.CharField(max_length = 10)
    Date_Published = models.DateField()
    Number_of_Pages = models.IntegerField()
    Date_of_Upload = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length = 100, unique = True , null=True)
    Picture = models.ImageField(upload_to = 'images/books/')
    About_Book = models.TextField()
    stock = models.IntegerField(null=True)
    is_available = models.BooleanField(default = True)
    Price = models.IntegerField(null=True)
    #modified_date = models.DateField(auto_add = True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    #the get_url function returns the url as specified and submits all  genre slugs and books slug of all book objects.
    # these are passed to the home.html to match the product variable with the same genre slug and book slug. 
    # Through this, theh product variable replaces the single_product_detail variable to access product details needed.
    def get_url(self):
        return reverse('bookapp:bookdetail', args=[self.Genre.slug, self.slug])
        
    def __str__(self):
        return self.Title