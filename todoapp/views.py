from django.urls import reverse_lazy
from .models import Mytodo
from .forms import TodoForm
from django.views.generic import CreateView, DeleteView, UpdateView

# Create your views here.

class alltodos(CreateView):
    template_name="alltodo.html"
    model = Mytodo
    form_class = TodoForm
    success_url = reverse_lazy('alltodos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = Mytodo.objects.all()
        return context

class deleteItem(DeleteView):
    template_name="deleteItem.html"
    model = Mytodo
    success_url = reverse_lazy('alltodos')

class updateItem(UpdateView):
    model = Mytodo
    fields = ['task']
    template_name="updateItem.html"
    success_url = reverse_lazy('alltodos')
