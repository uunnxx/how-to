from django.shortcuts import render
from .models import Order
from .forms import OrderForm


def index(request):
    object_list = Order.objects.all()
    form = OrderForm()
    # return render(request, './index.html', {'object_list': object_list})
    return render(request, './index.html', {'object_list': object_list, 'form': form})


def thanks_page(request):
    # name = request.GET['name']
    # phone = request.GET['phone']
    name = request.POST['name']
    phone = request.POST['phone']

    element = Order(order_name = name, order_phone = phone)
    element.save()

    return render(request, './thanks_page.html', {'name': name, 'phone': phone})
