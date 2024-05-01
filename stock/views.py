from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
# views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm

def index(request):
    # Logic for the index view
     return render(request, 'stock/index.html')

def stock(request):
    # Logic for the stock view
     return render(request, 'stock/get_started.html')

def view(request):
    return HttpResponse("this is view page")

def delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        item.delete()
        return redirect('list')  # Redirect to the item list page after deletion
    
    return render(request, 'stock/delete_confrimation.html', {'item': item})

def item_list(request):
    items = Item.objects.all()
    return render(request, 'stock/retrieve.html', {'items': items})

def update_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect to item list view after successful form submission
    else:
        form = ItemForm(instance=item)
    
    # Your update logic here (if any)
    
    return render(request, 'stock/update_item.html', {'form': form})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')  # Redirect to item list view after successful form submission
    else:
        form = ItemForm()
    
    return render(request, 'stock/add.html', {'form': form})