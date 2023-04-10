from django.shortcuts import render
from .models import MovieData
from django.core.paginator import Paginator
# Create your views here.

def movie_list(request):
    movies = MovieData.objects.all()
    movie_name = request.GET.get('movie_name')

    if movie_name != '' and movie_name is not None:
        movies = movies.filter(title__icontains=movie_name)


    paginator = Paginator(movies, 4)
    page = request.GET.get('page')
    movies = paginator.get_page(page)

    return render(request, 'newapp/movie_list.html', {'movies': movies})
    
  