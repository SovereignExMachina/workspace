from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Board


class Home(ListView):
    model = Board
    template_name = 'board/home.html'
    context_object_name = 'boards'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная'
        return context


class BoardDetail(DetailView):
    model = Board
    template_name = 'board/board_detail.html'
    context_object_name = 'board'
