from django.shortcuts import render, redirect
from django.http import HttpResponse
from restaurant.models import Inventory
from django.contrib import messages

# Create your views here.
def main(request):
    return render(request, 'main.html')

def inventory(request):
    all_inventory = Inventory.objects.all()
    return render(request, "inventory.html", {"all_inventory": all_inventory})

def menu(request):
    return render(request, "menu.html")

def recipe(request):
    return render(request, "recipe.html")

def purchase_log(request):
    return render(request, "purchase_log.html")

def add_inventory(request):
    if request.method == "POST":
        #Recieve Data
        name = request.POST["name"]
        quantity = request.POST["quantity"]
        price_per_unit = request.POST["price_per_unit"]

        #Save data
        inventory = Inventory.objects.create(
            name = name,
            quantity = quantity,
            price_per_unit = price_per_unit
        )
        inventory.save()
        messages.success(request, "Data Saved!")

        #redirect
        return redirect("/inventory")
    else:
        return render(request, "update_inventory.html")
    
def update_inventory(request, inv_id):
    if request.method == "POST":
        inventory = Inventory.objects.get(id=inv_id)
        inventory.name = request.POST["name"]
        inventory.quantity = request.POST["quantity"]
        inventory.price_per_unit = request.POST["price_per_unit"]
        inventory.save()
        messages.success(request, "Data Saved!")

        #redirect
        return redirect("/inventory")
    else:
        return render(request, "update_inventory.html")
    
def delete(request, inv_id):
    inventory = Inventory.objects.get(id=inv_id)
    inventory.delete()
    messages.success(request, "Data Deleted!")
    #redirect
    return redirect("/inventory")