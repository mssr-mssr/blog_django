from django.urls import path
from . import api_views

urlpatterns= [
    path('posts/', api_views.PostListCreateAPIView.as_view(), name='api_post_list'),
    path('posts/<int:pk>/', api_views.PostRetrieveUpdateDestroyAPIView.as_view(), name='api_post_detail')
]