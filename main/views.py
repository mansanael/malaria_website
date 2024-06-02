from django.shortcuts import render
from .models import Program, Activity, Ressource, Event
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['programs'] = Program.objects.all()
        context['activities'] = Activity.objects.all()
        context['ressources'] = Ressource.objects.all()
        context['events'] = Event.objects.all()
        return context
 
class AboutPageView(TemplateView):
    template_name = 'aboutus.html'

class ContactPageView(TemplateView):
    template_name = 'contactus.html'

class EmodPageView(TemplateView):
    template_name = 'emod.html'

class EventPageView(ListView):
    model = Event
    template_name = 'events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context

class HandBookPageView(TemplateView):
    template_name = 'handbook.html'

class ResourcesPageView(ListView):
    model = Ressource
    template_name = 'ressources.html'