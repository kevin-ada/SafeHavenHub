from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Events
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class EventForm(forms.ModelForm):
    description = forms.CharField(max_length=100)

    class Meta:
        model = Events
        fields = ['name', 'date', 'Location', 'description']


@method_decorator(login_required, name='dispatch')
class ListEvents(ListView):
    queryset = Events.objects.order_by('-created_on')
    template_name = 'components/events.html'
    context_object_name = 'events'

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_events')  # replace 'list_events' with the name of your events list view
        else:
            print(form.errors)
            # If the form is not valid, re-render the page with the form errors
            return render(request, 'components/schedule.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class ScheduleEvents(CreateView):
    template_name = 'components/schedule.html'
    model = Events
    form_class = EventForm
    context_object_name = 'form'
    success_url = reverse_lazy('list_events')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EventForm()  # add form instance to context
        return context
