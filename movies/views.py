from django.shortcuts import render, redirect
from django.views import View
from .models import *
from django.views.generic import ListView, DetailView
from .forms import ReviewForm
from django.db.models import Q


class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        years = Movie.objects.filter(draft=False).values('year')
        return years


class MoviesView(GenreYear, ListView):
    """список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(GenreYear, DetailView):
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


class FilterMoviesReview(GenreYear, ListView):
    """фильтр фильмов"""
    def get_queryset(self):
        year_list = self.request.GET.getlist('year')
        genres_list = self.request.GET.getlist('genres')
        print(year_list, genres_list)
        if year_list:
            if genres_list:
                queryset = Movie.objects.filter(year__in=year_list, genres__in=genres_list)
                return queryset
            else:
                queryset = Movie.objects.filter(year__in=year_list)
                return queryset
        else:
            queryset = Movie.objects.filter(genres__in=genres_list)
            return queryset















    # def get_queryset(self):
    #     queryset = Movie.objects.filter(
    #         Q(year__in=self.request.GET.getlist("year")) |
    #         Q(genres__in=self.request.GET.getlist("genres"))
    #     )
    #     return queryset







        # if year_list and genres_list == False:
        #     queryset = Movie.objects.filter(year__in=year_list)
        #     return queryset
        # elif genres_list and year_list == False:
        #     queryset = Movie.objects.filter(genres__in=genres_list)
        #     return queryset
        # else

