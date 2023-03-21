from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import MomentsToDocument
from .forms import AddingMomentForm,UpdatingMomentForm

# Create your views here.


class homepage(ListView):
	model = MomentsToDocument
	template_name = 'home.html'



class momentinformation(DetailView):
	model = MomentsToDocument
	context_object_name = 'x2'
	template_name = 'moment_information.html'


class addingamoment(CreateView):
	model = MomentsToDocument
	form_class = AddingMomentForm
	template_name = 'add_mymoment.html'

class updateamoment(UpdateView):
	model = MomentsToDocument
	context_object_name = 'x4'
	form_class = UpdatingMomentForm
	template_name = 'update_moment.html'


class deleteamoment(DeleteView):
	model = MomentsToDocument
	context_object_name = 'x3'
	template_name = 'delete_moment.html'
	success_url = reverse_lazy('home')
	
