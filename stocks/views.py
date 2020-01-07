from django.shortcuts import render
from django.http import JsonResponse
from .models import Order, Product, Type, Site


def create_post(request):
    posts = Order.objects.all()
    products = Product.objects.all()
    types = Type.objects.all()
    sites = Site.objects.all()

    response_data = {}

    if request.POST.get('action') == 'post':
        product1 = request.POST.get('product1')
        quantity1 = request.POST.get('quantity1')
        site1 = request.POST.get('site1')
        type1 = request.POST.get('type1')
        product2 = request.POST.get('product2')
        quantity2 = request.POST.get('quantity2')
        site2 = request.POST.get('site2')
        type2 = request.POST.get('type2')

        response_data['product1'] = product1
        response_data['quantity1'] = quantity1
        response_data['site1'] = site1
        response_data['type1'] = type1
        response_data['product2'] = product2
        response_data['quantity2'] = quantity2
        response_data['site2'] = site2
        response_data['type2'] = type2

        Order.objects.create(
            product1=Product.objects.get(name=product1),
            quantity1=quantity1,
            site1=Site.objects.get(name=site1),
            type1=Type.objects.get(name=type1),
            product2=Product.objects.get(name=product2),
            quantity2=quantity2,
            site2=Site.objects.get(name=site2),
            type2=Type.objects.get(name=type2),
         )
        return JsonResponse(response_data)
    return render(request, 'order_list.html', {'posts': posts, 'products': products, 'types': types, 'sites': sites})
