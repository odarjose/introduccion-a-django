from django.contrib import admin
from .models import Post
# Register your models here.
#de esta forma lo agregamos al panel del admin

admin.site.register(Post)