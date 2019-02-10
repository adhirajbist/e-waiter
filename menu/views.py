from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'menu/food_list.html', {'foods' : foods})

def cashier1(request):
     foods = Food.objects.filter(quantity__gt = 0)
     return render(request, 'menu/cashier.html', {'foods' : foods})

def food_edit(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            food = form.save(commit=False)
            food.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'menu/food_edit.html', {'form': form})
