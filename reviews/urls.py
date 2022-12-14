from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('danke', views.DankeReview.as_view()),
    path('reviews', views.ReviewListView.as_view()),
    path('reviews/favorite', views.AddFavoritesView.as_view()),
    path('reviews/<int:pk>', views.SingleReviewView.as_view()),

]
