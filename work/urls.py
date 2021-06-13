from django.urls import path
from . import views

app_name = 'work'

urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tags'),
    path('search/', views.post_list_by_search, name='search'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='post_create'),
    path('create_auto/', views.create_auto_post, name='post_create_auto'),

    path('news/<slug:news>/<int:news_id>/', views.newswork_detail, name='news_detail'),

    path('resume/<int:post_id>/', views.create_resume, name='resume_create'),
]
