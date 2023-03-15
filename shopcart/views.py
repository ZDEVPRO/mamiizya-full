from django.shortcuts import render, redirect
from shopcart.models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def cart_view(request):
    try:
        products = ShopCart.objects.filter(user=request.user)
        total_price = sum(product.amount for product in products)
        total_products = sum(product.quantity for product in products)

        for rs in products:
            if rs.product is None or rs.user is None:
                rs.delete()
                return redirect('cart')
            elif rs.product is None and rs.user is None:
                rs.delete()
                return redirect('cart')

        context = {
            'products': products,
            'total_price': total_price,
            'total_products': total_products
        }

        return render(request, 'cart.html', context)
    except Exception as e:
        print(e)
        return redirect('index')


@login_required(login_url='/login/')
def change_quantity(request, id):
    if request.method == 'GET':
        quantity = request.GET.get('quantity')

        product = ShopCart.objects.get(id=id)
        product.quantity = int(quantity)
        product.save()
        return redirect('cart')


@login_required(login_url='/login/')
def remove_cart(request, id):
    product = ShopCart.objects.get(id=id)
    product.delete()
    return redirect('cart')


def info_view(request, id):
    product = Product.objects.get(id=id)
    sizes = product.size.all()
    colors = product.color.all()

    context = {
        'product': product,
        'sizes': sizes,
        'colors': colors
    }
    return render(request, 'info.html', context)


@login_required(login_url='/login/')
def add_cart(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        color = request.POST.get('product_color')
        quantity = request.POST.get('product_quantity')
        size = request.POST.get('product_size')

        try:
            cart_item = ShopCart.objects.get(product__id=product.id, color=color, size=size)
            total_quantity = cart_item.quantity + int(quantity)
            cart_item.quantity = total_quantity
            cart_item.save()
            return redirect('cart')
        except Exception as e:
            print(e)
            cart = ShopCart()
            cart.user = request.user
            cart.product = product
            cart.quantity = quantity
            cart.size = size
            cart.color = request.POST.get('product_color')
            cart.save()
            return redirect('cart')


@login_required(login_url='/login/')
def buy_products(request):
    cart_products = ShopCart.objects.filter(user=request.user)
    total_price = sum(product.amount for product in cart_products)
    total_products = sum(product.quantity for product in cart_products)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')

        region = request.POST.get('region')
        district = request.POST.get('district')
        address = request.POST.get('address')
        client_notes = request.POST.get('client_notes')

        order = Order()
        order.user = request.user
        order.first_name = first_name
        order.last_name = last_name
        order.phone_number = phone_number
        order.region = region
        order.district = district
        order.address = address
        order.client_notes = client_notes
        order.save()

        for rs in cart_products:
            order_item = OrderItem()
            order_item.product = rs.product
            order_item.order = order

            order_item.title = rs.product.title
            order_item.image = rs.product.image
            order_item.price = rs.product.price
            order_item.quantity = rs.quantity
            order_item.color = rs.color
            order_item.size = rs.size
            order_item.save()

            rs.delete()

        return redirect('success-page')

    context = {
        'cart_products': cart_products,
        'total_price': total_price,
        'total_products': total_products
    }

    return render(request, 'buy_product.html', context)


def success_page(request):
    return render(request, 'components/success_page.html')
