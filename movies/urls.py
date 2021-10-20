from django.urls import path
from . import views

urlpatterns = [
    path('', views.MoviesView.as_view(), name='movies'),
    path('filter/', views.FilterMoviesReview.as_view(), name='filter'), # filter ставится перед slug, чтобы он не попадал под шаблон поиска фильма по slug
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),
]