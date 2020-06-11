from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
urlpatterns=[
    path('',views.home,name='blog-saatvik'),
    path('about-us/',views.about,name='about-page'),
    path('contact-us/',views.contact,name='contact-page'),
    path('post/',PostListView.as_view(),name='blog-saatvik'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='blog-detail'),
    path('post/create/',PostCreateView.as_view(),name='blog-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='blog-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='blog-delete'),
    path('post/<str:username>/',UserPostListView.as_view(),name='user-post'),
]

#post_confirm_delete.html