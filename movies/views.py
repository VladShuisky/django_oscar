from django.shortcuts import render, redirect
from django.views import View
from .models import Movie
from django.views.generic import ListView, DetailView
from .forms import ReviewForm


class MoviesView(ListView):
    """список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/movie_list.html", {"movies_list": movies})


class MovieDetailView(DetailView):
    """Подробности о фильме"""
    model = Movie
    slug_field = 'url'
    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     print(movie.description)
    #     return render(request, "movies/movie_detail.html", {"movie": movie})


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
