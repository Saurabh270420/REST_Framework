# from django.http import JsonResponse
from rest_framework.response import Response
from movies.models import Movies
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from movies.api.serializers import MovieSerializer

class movie_list(APIView):
    def get(self,request):
        movies=Movies.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)

class movie_details(APIView):
    def get(self,request,pk):
        movie=Movies.objects.get(pk=pk)
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Movies.objects.get(pk=pk)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    
    def delete(self,request,pk):
        movie=Movies.objects.get(pk=pk)
        movie.delete()

        





# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movies.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)

# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
#     if request.method=='GET':
#         movie=Movies.objects.get(pk=pk)
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method=='PUT':
#         movie=Movies.objects.get(pk=pk)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)
        
#     if request.method=='DELETE':
#         movie=movie=Movies.objects.get(pk=pk)
#         movie.delete()
#         return Response({'data':"Deleted successfully"})
