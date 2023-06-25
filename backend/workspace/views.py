from django.shortcuts import redirect, render, get_object_or_404
from .models import WorkSpace, Task, Column
from .forms import WorkSpaceForm


def show_workspace(request):
    ws = WorkSpace.objects.all()
    context = {
        'workspace': ws,
    }
    return render(request, template_name='workspace/workspace.html', context=context)


def get_workspace(request, ws_id):
    ws_all = WorkSpace.objects.all()
    ws = get_object_or_404(WorkSpace, pk=ws_id)
    context = {
        'workspace_item': ws,
        'workspace': ws_all,
    }
    return render(request, template_name='workspace/workspace_detail.html', context=context)


def create_workspace(request):
    if request.method  == 'POST':
        form = WorkSpaceForm(request.POST)
        if form.is_valid():
            ws = form.save()
            return redirect(ws)
    else:
        form = WorkSpaceForm()
    return render(request, template_name='workspace/create_workspace.html', context={'ws_form': form})