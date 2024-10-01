from django.shortcuts import render
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'app/index.html'
    # context_object_name = 'items'
    # login_url = '/hello'
    # redirect_field_name = 'redirect_to'

    def get_queryset(self):
        return []

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     context['is_superuser'] = self.request.user.is_superuser
    #     context['current_site'] = Site.objects.get_current()
    #     return context