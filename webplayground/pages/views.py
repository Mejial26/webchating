from typing import Any
from django import http
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .models import Page
from .forms import PageForm

# Create your views here.

class Staffrequired():
    """
    Esto es un mixin de usuario requerido, para heredar en las demas clases
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.is_staff:
        #     return redirect(reverse_lazy('admin:login'))
        return super().dispatch(request, *args, **kwargs)

class Pagelistview(ListView):
    model = Page    


class PageDetailView(DetailView): 
    model = Page
    template_name = "pages/page.html"


@method_decorator(staff_member_required,name='dispatch')
class PageCreateview(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    
    
@method_decorator(staff_member_required,name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'
    
    
@method_decorator(staff_member_required,name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')



