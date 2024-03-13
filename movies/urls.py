from django.urls import path
from movies.api.views import movie_list,movie_details
urlpatterns = [
    path('list',movie_list.as_view()),
    path('<int:pk>',movie_details.as_view())
]
