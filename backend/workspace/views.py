from typing import Any, Dict
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, View
from .models import WorkSpace, Task, Column
from .forms import WorkSpaceForm, ColumnForm, TaskForm


class WorkSpaceView(ListView):
    model = WorkSpace
    template_name = 'workspace/workspace.html'
    context_object_name = 'workspaces'


class WorkSpaceDetail(DetailView):
    model = WorkSpace
    template_name = 'workspace/workspace_detail.html'
    context_object_name = 'workspace_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workspaces'] = WorkSpace.objects.all()
        return context


class WorkSpaceCreate(CreateView):
    form_class = WorkSpaceForm
    template_name = 'workspace/create_workspace.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['workspaces'] = WorkSpace.objects.all()
        return context


class ColumnCreate(View):
    def get(self, request, pk):
        ws = WorkSpace.objects.get(id=pk)
        form = ColumnForm()
        return render(request, template_name='workspace/create_column.html', context={'workspace': ws, 'form': form})

    def post(self, request, pk):
        ws = WorkSpace.objects.get(id=pk)
        form = ColumnForm(request.POST)
        if form.is_valid():
            column = form.save()
            ws.column.add(column)
            return redirect(ws.get_absolute_url())
        return render(request, template_name='workspace/create_column.html', context={'workspace': ws, 'form': form})


class TaskCreate(View):
    def get(self, request, pk):
        column = Column.objects.get(id=pk)
        form = TaskForm()
        return render(request, template_name='workspace/create_task.html', context={'column': column, 'form': form})
    
    def post(self, request, pk):
        column = Column.objects.get(id=pk)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            column.task.add(task)
            return redirect('workspace:home')
        return render(request, template_name='workspace/create_task.html', context={'column': column, 'form': form})