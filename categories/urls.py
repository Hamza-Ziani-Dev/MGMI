from django.urls import include, path

from . import views

app_name='categories'

urlpatterns = [
    path('categories/',views.categories , name='categories'),
]