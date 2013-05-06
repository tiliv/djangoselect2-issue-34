from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy

from .models import Employee
from .forms import EmployeeForm

class TestListView(ListView):
    model = Employee

class TestCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super(TestUpdateView, self).get_context_data(**kwargs)
        context['field_class_name'] = context['form'].fields['store'].__class__.__name__
        return context

class TestUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('list')

    def get_context_data(self, **kwargs):
        context = super(TestUpdateView, self).get_context_data(**kwargs)
        context['field_class_name'] = context['form'].fields['store'].__class__.__name__
        return context
