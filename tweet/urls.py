from django.urls import path
from tweet.views import home_view, tweet_detail_view

urlpatterns = [
    path('', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),
]
