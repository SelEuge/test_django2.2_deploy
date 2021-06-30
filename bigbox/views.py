from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Box, Activity
from django.conf import settings


# Create your views here.
# 4) a
class ListAllBoxes(ListView):
    template_name = 'list_all_boxes.html'
    model = Box
    context_object_name = 'boxes'


def home(request):
    boxes = Box.objects.all()
    return render(request, 'list_all_boxes.html', {'boxes': boxes})


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
    paginate_by = settings.PAGINADOR

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
def SearchBoxBySlug(request, slug):
    box = Box.objects.get(slug=slug)
    print(box)
    return render(request, 'detailsxslug.html', {'boxes_bySlug': box})
