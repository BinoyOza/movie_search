# Movie Search
This repository contains the code for Django Rest Framework based implementation of movie search tool.

It contains an API that allows consumers to access the movies data. Most of the queries will be
against local database but you need to get the data from imdb open api
(http://www.omdbapi.com/) to query for movies when data isn’t available in the local database
and store it for future reference. Movie object in database will have following properties as well
as movie object in response of the apis:

- title
- released year
- rating
- id
- genres (array of strings)

For Storing the values from API:
- Find movie by title by exact value that’s passed in the API. Notes: If there is no match in local
database, use omdb-api service for the search. If that returns result(s), then store the result in
database and return first value.

API Contains following searching options:
1. Search by Id.
2. Search movies released in a particular year.
3. Search movies with rating higher than passed in value.
4. Search movies with passed in genres value.

The Postman collection with the example can be referred over the link: https://www.getpostman.com/collections/024352f7d69f73f129f7
