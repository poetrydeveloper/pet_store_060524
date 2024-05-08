from django.shortcuts import render, get_object_or_404
from .models import Tool


def tool_list(request):
    tools = Tool.objects.all()
    return render(request,
                  'store/tool/list.html',
                  {'store': tools})


def tool_detail(request, id):
    tool = get_object_or_404(Tool,
                             id=id)
    return render(request,
                  'store/tool/detail.html',
                  {'tool': tool})
