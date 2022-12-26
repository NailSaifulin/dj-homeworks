from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    name_phone = request.GET.get("sort")
    if name_phone == 'min_price':
        phone_items = Phone.objects.order_by('price').all()
    elif name_phone == 'max_price':
        phone_items = Phone.objects.order_by('-price').all()
    elif name_phone:
        phone_items = Phone.objects.filter(name=name_phone).all()
    else:
        phone_items = Phone.objects.all()
    context = {'phones': phone_items}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_item = Phone.objects.filter(slug=slug).first()
    context = {'phone': phone_item}
    return render(request, template, context)
