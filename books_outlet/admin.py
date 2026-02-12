from django.contrib import admin
from .models import Books, Author, Country
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", )
    list_filter = ("first_name", "last_name", )


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    list_filter = ("name", )


class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", )
    list_filter = ("author", "is_bestseller", "published_countries", "rating", )
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Books, BooksAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Country)