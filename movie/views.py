import requests

from rest_framework import viewsets

from .serializers import MovieSerializer
from .models import Movie
from .constants import API_KEY

API_URL = "https://www.omdbapi.com/?apikey=" + API_KEY


def get_from_api(title):
    queryset = Movie.objects.filter(title=title)
    if not queryset:
        response = requests.get(API_URL + "&s=" + title)
        if response.status_code == 200:
            movies = []
            for movie in response.json().get("Search"):
                movie_response = requests.get(API_URL + "&i=" + movie.get("imdbID"))
                if movie_response.status_code == 200:
                    rating = 0 if movie_response.json().get("imdbRating") == "N/A" else movie_response.json().get(
                        "imdbRating")
                    movies.append(
                        Movie(
                            imdb_id=movie_response.json().get("imdbID"),
                            title=movie_response.json().get("Title"),
                            released_year=movie_response.json().get("Year"),
                            rating=rating,
                            genre=movie_response.json().get("Genre")
                        )
                    )
            if movies:
                Movie.objects.bulk_create(movies)
                return movies[:1]
        return None
    else:
        return queryset


class MovieViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        title = self.request.query_params.get('title')
        id = self.request.query_params.get('id')
        year = self.request.query_params.get('year')
        rating = self.request.query_params.get('rating')
        genre = self.request.query_params.get('genre')
        queryset = Movie.objects.all()
        if title:
            queryset = get_from_api(title)
        elif id:
            queryset = Movie.objects.filter(imdb_id=id)
        elif year:
            queryset = Movie.objects.filter(released_year=int(year))
        elif rating:
            queryset = Movie.objects.filter(rating__gte=int(rating))
        elif genre:
            queryset = Movie.objects.filter(genre__icontains=genre)
        return queryset

    serializer_class = MovieSerializer
    model = Movie
