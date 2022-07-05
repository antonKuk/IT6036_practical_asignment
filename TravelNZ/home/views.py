from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Tour, Agent
from django.urls import reverse_lazy


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home/home.html'


class AgentListView(ListView):
    queryset = Agent.objects.all().order_by('agent_username')
    # setup template file
    template_name = 'home/agents.html'
    context_object_name = 'agents'

    # setup how many data to display per page
    paginate_by = 10

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'home/agent_detail.html'
    context_object_name = 'agent'

class AgentUpdateView(UpdateView):
    model = Agent
    fields = ['agent_username', 'email_address']
    template_name = 'home/agent_edit.html'
    context_object_name = 'agent_edit'


class AgentDeleteView(DeleteView):
    model = Agent
    template_name = 'home/agent_delete.html'


class TourListView(ListView):
    queryset = Tour.objects.all().order_by('tour_name')

    # setup template file
    template_name = 'home/tours.html'

    # setup “friendly” template context
    # if not set up, 'tour_list' used as default
    # setting 'context_object_name' is always a good idea
    context_object_name = 'tours'

    # setup how many data to display per page
    paginate_by = 10


class TourDetailView(DetailView):
    queryset = Tour.objects.all().order_by('tour_name')

    template_name = 'home/tour_detail.html'

    context_object_name = 'tour'

class TourUpdateView(UpdateView):
    queryset = Tour.objects.all().order_by('tour_name')
    fields = ['tour_name', 'duration', 'description', 'available']
    template_name = 'home/tour_edit.html'

    context_object_name = 'tour_edit'

class TourDeleteView(DeleteView):
    model = Tour
    template_name = 'home/tour_delete.html'

    context_object_name = 'tour_delete'


# def tours_by_agent(self, request):
#     # request.user_set.all()
#     logged_in_user = request.user
#     logged_in_user_tours = Tour.objects.filter(agent=logged_in_user)
#     return render(request, 'home/tours_by_agent.html', {'tours': logged_in_user_tours})


class AgentToursListView(ListView):
    model = Tour
    template_name = 'home/tours_by_agent.html'
    context_object_name = 'tours'

    def get_queryset(self):
        agent_pk = get_object_or_404(Agent,pk=self.kwargs.get('pk'))
        return Tour.objects.filter(agent_id=agent_pk)
