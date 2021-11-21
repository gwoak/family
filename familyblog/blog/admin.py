from django.contrib import admin
from .models import Post, Category, Profile

# Apply summernote to all TextField in model.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)

