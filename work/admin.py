from django.contrib import admin
from .models import Post, Newswork, Resume

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''pass'''
    list_display = ('title', 'publish', 'status', 'slug', 'specialization', 'size_company')
    list_filter = ('publish', 'status')
    # search_fields = ('agent', 'id')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Newswork)
class NewsAdmin(admin.ModelAdmin):
    '''pass'''
    list_display = ('title', 'update', 'status')
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    '''pass'''
    list_display = ('email', 'post', 'publish', 'slug')
    list_filter = ('status',)
    search_fields = ('email',)
    prepopulated_fields = {'slug': ('first_name','last_name',)}
