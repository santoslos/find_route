from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from cities.forms import CityForm
from cities.models import City

__all__ = ('home', 'CityDetailView', 'test', 'CityCreateView',
           'CityUpdateView', 'CityDeleteView', 'CityListView',)


def home(request, pk=None):
    # if pk:
    #     city = City.objects.filter(id=pk).first
    #
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
    form = CityForm()
    qs = City.objects.all()
    lst = Paginator(qs, 5)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj, 'form': form}
    return render(request, 'cities/home.html', context)


def test(request):
    return render(request, 'cities/test.html')


class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
    pk_url_kwarg = 'pk_city'


class CityListView(ListView):
    queryset = City.objects.all()
    template_name = 'cities/list.html'
    paginate_by = 2


class CityCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'
    success_url = reverse_lazy('cities:home')
    success_message = "Город успешно создан"


class CityUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')
    pk_url_kwarg = 'pk_city'
    success_message = "Город успешно отредактирован"


class CityDeleteView(LoginRequiredMixin, DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')
    pk_url_kwarg = 'pk_city'

    def get(self, request, *args, **kwargs):
        messages.success(request, 'Город удален')
        return self.post(request, *args, **kwargs)
