from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:survey_page_id>/", views.detail, name='index'),
    path("<int:survey_page_id>/results/", views.results, name='index'),
    path("<int:survey_page_id>/vote/", views.vote, name='index'),
#   path('survey/', views. name=''),
]