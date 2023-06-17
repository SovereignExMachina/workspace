from django.shortcuts import render
from .models import WorkSpace, Task, Column


def show_workspace(request):
    workspace = WorkSpace.objects.all()
    context = {
        'workspace': workspace,
    }
    return render(request, template_name='workspace/workspace.html', context=context)
