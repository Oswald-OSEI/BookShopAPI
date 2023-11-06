from django.contrib import admin
from .models import Genre, Books, Authors
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('Title',)}
    list_display = ('Title','slug', 'uploader', 'Date_of_Upload')
    readonly_fields = ('uploader', 'Date_of_Upload',)
    ordering = ('Date_of_Upload',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
   
admin.site.register(Books, BookAdmin) 


class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('genre',)}
    list_display=('genre', 'slug')
admin.site.register(Genre, GenreAdmin)

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('first_name', 'last_name',)}
    list_display=('first_name', 'last_name', 'slug')
admin.site.register(Authors, AuthorAdmin)

