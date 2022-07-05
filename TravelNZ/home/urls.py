from django.urls import path

from .views import HomePageView, AgentListView, TourListView, TourDetailView, AgentDetailView, AgentToursListView, AgentUpdateView, TourUpdateView, TourDeleteView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('agents/', AgentListView.as_view(), name='agents'),
    path('agents/<int:pk>/', AgentDetailView.as_view(), name='agent_detail'),
    path('agents/<int:pk>/edit', AgentUpdateView.as_view(), name='agent_edit'),
    path('agents/<int:pk>/tours/', AgentToursListView.as_view(), name='tours_by_agent'),
    path('tours/', TourListView.as_view(), name='tours'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour_detail'),
    path('tours/<int:pk>/edit', TourUpdateView.as_view(), name='tour_edit'),
    path('tours/<int:pk>/delete', TourDeleteView.as_view(), name='tour_delete'),
    # path('tours/<int:pk>/delete', TourDeleteView.as_view(), name='tour_delete'),
]