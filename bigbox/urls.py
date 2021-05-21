# from django.contrib.admin import admin
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    # path('listarboxes', views.ListarBoxesView.as_view()),
    # path('box', views.ListAllBoxes.as_view(), name="boxes"),
    path('box', home, name="boxes"),
    path('box/<int:box_id>/', views.DetailBox.as_view(), name="box"),
    path('box/<box_id>/activity', views.ListActivitiesByBox.as_view(), name="activities"),
    path('box/<box_id>/activity/<activity_id>/', views.ShowActivityByBox.as_view(), name='activitydetail'),
    path('box/<slug:slug>/', SearchBoxBySlug, name="boxes_bySlug"),
]
