from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView, ListView

#from tr.forms import TrainForm
from trains.models import Train

__all__ = ('home', 'TrainDetailView', 'test', 'TrainCreateView',
           'TrainUpdateView', 'TrainDeleteView', 'TrainListView',)


def home(request, pk=None):
    # if pk:
    #     Train = Train.objects.filter(id=pk).first
    #
    #     context = {'object': Train}

    qs = Train.objects.all()
    lst = Paginator(qs, 2)
    page_number = request.GET.get('page')
    page_obj = lst.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'trains/home.html', context)


def test(request):
    return render(request, 'trains/test.html')


class TrainDetailView(DetailView):
    queryset = Train.objects.all()
    template_name = 'trains/detail.html'
    pk_url_kwarg = 'pk_Train'


class TrainListView(ListView):
    queryset = Train.objects.all()
    template_name = 'trains/list.html'
    paginate_by = 2


class TrainCreateView(SuccessMessageMixin, CreateView):
    model = Train

    template_name = 'trains/create.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Город успешно создан"


class TrainUpdateView(SuccessMessageMixin, UpdateView):
    model = Train

    template_name = 'trains/update.html'
    success_url = reverse_lazy('trains:home')
    success_message = "Город успешно отредактирован"
    pk_url_kwarg = 'pk_Train'

class TrainDeleteView(DeleteView):
    model = Train
    template_name = 'trains/delete.html'
    success_url = reverse_lazy('trains:home')
    pk_url_kwarg = 'pk_Train'
    def get(self, request, *args, **kwargs):
        messages.success(request, "Город успешно удален")
        return self.post(request, *args, **kwargs)
