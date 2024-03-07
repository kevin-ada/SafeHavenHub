from django.urls import path
from .views import ListEvents, ScheduleEvents

urlpatterns = [
    path('events/', ListEvents.as_view(), name='list_events'),
    path('events/create/', ScheduleEvents.as_view(), name='eventcreate'),
]
