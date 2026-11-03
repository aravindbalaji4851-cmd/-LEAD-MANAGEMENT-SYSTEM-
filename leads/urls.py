from django.urls import path

from leads.views import LeadCreateListView
from leads.views import LeadRetrieveUpdateDestroyView

urlpatterns = [

    path('',LeadCreateListView.as_view()),
    path('<int:pk>/',LeadRetrieveUpdateDestroyView.as_view()),    
]