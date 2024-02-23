from django.shortcuts import render
from .form import StudentForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import User
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'forms.html'
    success_url = '/'

class StudentListView(ListView):
    model = User 
    template_name = 'getdata.html'
    context_object_name = 'stu'

class StudentUpdateView(UpdateView):
    model = User
    form_class = StudentForm
    template_name = 'forms.html'
    success_url = '/data-show/'

class StudentDeleteView(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = '/data-show/'

#####################################
# Student Single Object list Details
    
class StudentDetailView(DetailView):
    model = User
    template_name = 'singleObjectDetail.html'
    context_object_name = 'stu'
    success_url = '/data-show/'