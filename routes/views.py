from django.contrib import messages
from django.shortcuts import render
from routes.forms import RouteForm


# Create your views here.

def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == "POST":
        form = RouteForm(request.POST)
        a = 1

    else:
        form = RouteForm()
        messages.error(request, "Нет данных для поиска")
    return render(request, 'routes/home.html', {'form': form})
