from typing import List
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import School, Student


class SchoolListView(ListView):
    model = School


class SchoolDetailView(DetailView):
    model = School
    template_name = "basic_app/school_detail.html"
