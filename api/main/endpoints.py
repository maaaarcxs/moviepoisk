from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import MovieSerializer, GenreSerializer
from moviesearch.models import Movie, Genre


@api_view(['GET'])
def movies_list(request):
    movies = Movie.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(movies, request)
    serializer = MovieSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def movies_create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        object = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'detail': 'Not found'})
    
    if request.method == "GET":
        serializer = MovieSerializer(object, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MovieSerializer(object, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)
    
    if request.method == "DELETE":
        object.delete()
        return Response(status=204)
    

@api_view(['GET'])
def genres_list(request):
    movies = Movie.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 12

    result_page = paginator.paginate_queryset(movies, request)
    serializer = MovieSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['POST'])
def movies_create(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.error, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try:
        object = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'detail': 'Not found'})
    
    if request.method == "GET":
        serializer = MovieSerializer(object, many=False)
        return Response(serializer.data)

    if request.method == "PUT":
        serializer = MovieSerializer(object, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)
    
    if request.method == "DELETE":
        object.delete()
        return Response(status=204)