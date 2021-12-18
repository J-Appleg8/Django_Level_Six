from typing import List
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import School, Student


class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    context_object_name = "schools"
    model = School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    model = School
    fields = ("name", "principal", "location")


class SchoolUpdateView(UpdateView):
    model = School
    fields = ("name", "principal")


class SchoolDeleteView(DeleteView):
    model = School

    success_url = reverse_lazy("basic_app:list")
