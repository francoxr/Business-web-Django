from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    # show fields in columns
    list_display = ('title', 'author', 'publised', 'post_categories')
    # ordering the records
    ordering = ('author', 'publised')
    # add a search bar
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    #

    # add filter bar
    list_filter = ('author__username','categories__name')
    
    def post_categories(self, obj):
        print(obj.categories.all())
        return ", ".join([c.name for c in obj.categories.all()])
    
    post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)