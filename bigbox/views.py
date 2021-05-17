from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Box, Activity


# Create your views here.
# 4) a
class ListAllBoxes(ListView):
    template_name = 'list_all_boxes.html'
    model = Box
    context_object_name = 'boxes'


# 4) b) i
class DetailBox(ListView):
    template_name = 'detail_box.html'
    paginate_by = 5

    def get_queryset(self):
        box_id = self.kwargs['box_id']
        # context_object_name = 'boxes'
        box = Box.objects.filter(id=box_id)
        return box


# 4) c) i
class ListActivitiesByBox(ListView):
    template_name = 'list_activities_by_box.html'
    context_object_name = 'activities'
    paginate_by = 20

    def get_queryset(self):
        box_id = self.kwargs['box_id']
        box = Box.objects.get(id=box_id)
        return box.activities.all()


# 4) d) i
class ShowActivityByBox(ListView):
    template_name = 'show_activity_by_box.html'

    # context_object_name = 'activities'

    def get_queryset(self):
        box_id = self.kwargs['box_id']
        activity_id = self.kwargs['activity_id']
        box = Box.objects.get(id=box_id)
        return box.activities.filter(id=activity_id)


# 5) c) i
class SearchBoxBySlug(ListView):
    template_name = 'detail_box.html'
    # queryset = Box.objects.filter(slug='prueba')
    model = Box

    def get_queryset(self):
        return Box.objects.filter(slug=self.kwargs['slug'])

    """def get_queryset(self):
        slug = self.kwargs['slug']
        # context_object_name = 'boxes'
        boxes = Box.objects.filter(slug=slug)
        return Box.objects.filter(slug=slug)"""
