from django.shortcuts import render
from .forms import FoodItemForm


# Create your views here.
def index(request):
    form = FoodItemForm()
    return render(request, "dailycount/index.html", {"form": form})


def food_item_view(request):
    form = FoodItemForm()
    return render(request, "index.html", {"form": form})
