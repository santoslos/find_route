from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from cities.forms import CityForm, CityForm
from cities.models import City

__all__ = ('home', 'CityDetaulView', 'test')


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
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


def test(request):
    return render(request, 'cities/test.html')


class CityDetaulView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'
