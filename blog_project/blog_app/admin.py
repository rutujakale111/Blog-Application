from django.contrib import admin
from .models import Post

# Create a custom admin class for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('title', 'content', 'author__username')  # Allow searching by title, content, and author username
    list_filter = ('created_at', 'author')  # Add filters by created date and author
    ordering = ('-created_at',)  # Order posts by creation date in descending order
    date_hierarchy = 'created_at'  # Allow filtering posts by date hierarchy
    fields = ('title', 'content', 'author')  # Display these fields when adding/editing posts
    readonly_fields = ('created_at', 'updated_at')  # Make created_at and updated_at read-only

# Register the Post model and the custom PostAdmin class
admin.site.register(Post, PostAdmin)