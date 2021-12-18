from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
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
