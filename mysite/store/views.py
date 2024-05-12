from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Tool


class ToolListView(ListView):
    """
    Альтернативное представление списка постов
    """
    queryset = Tool.objects.all()
    context_object_name = 'tools'
    paginate_by = 3
    template_name = 'store/tool/list.html'


def tool_detail(request, id):
    tool = get_object_or_404(Tool,
                             id=id)
    return render(request,
                  'store/tool/detail.html',
                  {'tool': tool})
