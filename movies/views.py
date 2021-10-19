from django.shortcuts import render, redirect
from django.views import View
from .models import Movie, Category, Actor
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class MoviesView(ListView):
    """список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Подробности о фильме"""
    model = Movie
    slug_field = 'url'

class ActorView(DetailView):
    """Подробности об актере/режиссере"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
        form.movie = movie
        form.save()
        print(form._meta.fields)
        return redirect(movie.get_absolute_url())
