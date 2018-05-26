
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Item,ShoppingCart,ItemQuantity
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseNotFound

import string, random


def index(request):


    cat = [i[0] for i in Item.CATEGORIES]
    context = {
        'category': cat,
    }
    return render(request, 'ykea/home.html', context)

def items(request,category=""):
    items_by_category = Item.objects.filter(category=category)
    context = {
        'items': items_by_category,
        'category': category,
    }
    return render(request, 'ykea/items.html', context)


def details(request,id):

    try:
        item = Item.objects.get(item_number = id)

        context = {
        'item' : item,

        }
    except Item.DoesNotExist: #Habria que mandar a un 404 o algo
        return HttpResponseNotFound('<h1>Item not found</h1>')


    return render(request, 'ykea/details.html', context)


# part2
def shoppingcart(request):
    if "selectedItem" in request.session:
    	  selectedItems = request.session["selectedItem"]
    else:
        selectedItems = []
    for key in request.POST:
        if key.startswith("checkbox"):
            selectedItems.append(request.POST[key])
    request.session["selectedItem"] = selectedItems

    if "cart" in request.session:
        cart = ShoppingCart.objects.get(cart_id = request.session["cart"])
    else:
        cart = ShoppingCart.objects.create()
        request.session["cart"] = cart.cart_id

    print(set(selectedItems))
    for it in set(selectedItems):
        i = Item.objects.get(item_number=it)
        if ItemQuantity.objects.filter(cart=cart,item = i).count() == 0:
            ItemQuantity.objects.create(item=i, cart=cart)
        else:
            itemq = ItemQuantity.objects.get(item=i,cart=cart)
            itemq.quantity +=1
            itemq.save()


    return HttpResponseRedirect(reverse('buy'))


def buy(request):
    cart = ShoppingCart.objects.get(cart_id = request.session["cart"])
    listItems = ItemQuantity.objects.filter(cart=cart)

    price = 0
    for i in set(listItems):
        price += (i.item.price * i.quantity)


    context = {
        'items': listItems,
        'price': price,
    }


    return render(request, 'ykea/shoppingcart.html', context)


def process(request):
    if request.POST.get("delete"):
        return HttpResponseRedirect(reverse('delete'))
    elif request.POST.get("checkout"):
        return HttpResponseRedirect(reverse('checkout'))



def delete(request):
    return HttpResponse("<h1>DELET THIS</h1>")


def checkout(request):
    return HttpResponse('<h1>CHECKOUT THIS</h1>')

