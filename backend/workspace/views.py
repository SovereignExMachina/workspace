from django.shortcuts import render
from .models import WorkSpace, Task, Column


def show_workspace(request):
    workspace = WorkSpace.objects.all()
    contex = {
        'workspace': workspace,
    }
    return render(request, template_name='workspace/workspace.html', context=contex)
