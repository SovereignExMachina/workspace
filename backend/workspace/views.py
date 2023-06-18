from django.shortcuts import render, get_object_or_404
from .models import WorkSpace, Task, Column


def show_workspace(request):
    ws = WorkSpace.objects.all()
    context = {
        'workspace': ws,
    }
    return render(request, template_name='workspace/workspace.html', context=context)


def get_workspace(request, ws_id):
    ws = get_object_or_404(WorkSpace, pk=ws_id)
    context = {
        'workspace_item': ws,
    }
    return render(request, template_name='workspace/workspace_detail.html', context=context)
