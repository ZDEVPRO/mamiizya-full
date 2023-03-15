import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from home.models import *
from site_settings.models import *
from django.core.paginator import Paginator
from datetime import timedelta, timezone, datetime
from home.forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from shopcart.models import *
from Sections.models import *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    home_slider = HomeSlider.objects.all()
    section5to8 = Section5to8.objects.all()
    section9to10 = Section9to10.objects.all()
    section11plus = Section11Plus.objects.all().order_by('-id')

    context = {
        'home_slider': home_slider,
        'section5to8': section5to8,
        'section9to10': section9to10,
        'section11plus': section11plus
    }
    return render(request, 'home.html', context)


def shop(request):
    products = Product.objects.all().order_by('-id')
    p = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    count = products.count()
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        if keyword == 'all':
            return redirect('shop')
        else:
            return redirect('filter', keyword)

    context = {
        'products': products,
        'count': count,
        'page_obj': page_obj
    }
    return render(request, 'shop.html', context)


def about(request):
    about_data = About.objects.last()
    context = {
        'about': about_data
    }

    return render(request, 'about.html', context)


def contact(request):
    contact_data = ContactData.objects.last()
    bot_data = TelegramBot.objects.last()

    if request.method == 'POST':
        data = Contact()
        data.first_name = request.POST.get('first_name')
        data.last_name = request.POST.get('last_name')
        data.phone = request.POST.get('phone')
        data.message = request.POST.get('message')
        data.ip = get_client_ip(request)
        data.create_at = datetime.now()
        data.save()
        messages.success(request, 'Xabaringiz muvoffaqiyatli yetkazildi! Sizga qisqa muddat ichida aloqaga chiqamiz!')

        tm = datetime.now() + timedelta(hours=3)
        time = tm.strftime("%H:%M")

        text = f'🇺🇿 YANGI XABAR KELDI! 🇺🇿 \n' \
               f'\n 👨  FISH: {data.first_name} {data.last_name}' \
               f'\n 📲  Telefon raqam: {data.phone}' \
               f'\n 🌐  IP RAQAM: {data.ip}' \
               f'\n 🕒  VAQT: {time}' \
               f'\n 📆  SANA: {data.create_at.strftime("%d-%m-%Y")}' \
               f'\n 📩  XABAR: {data.message}'
        text1 = "".join(text)

        bot_token = bot_data.bot_token
        bot_chatID = bot_data.chat_id

        url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={text1}'

        response = requests.get(url)

    context = {
        'contact': contact_data
    }

    return render(request, 'contact.html', context)


def shop_detail(request, id):
    product = Product.objects.get(id=id)
    images = ImageItem.objects.filter(product__id=id)
    sizes = product.size.all()
    colors = product.color.all()

    if request.method == 'POST':
        amount = request.POST.get('amount')
        print(amount)

    context = {
        'product': product,
        'images': images,
        'sizes': sizes,
        'colors': colors
    }

    return render(request, 'shop_detail.html', context)


def filter_view(request, keyword):
    if keyword == 'all':
        products = Product.objects.all().order_by('-id')
    else:
        products = Product.objects.filter(category__link=keyword).order_by('-id')
    p = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    count = products.count()
    context = {
        'products': products,
        'keyword': keyword,
        'page_obj': page_obj,
        'count': count
    }
    return render(request, 'filter.html', context)


def search_view(request):
    try:
        if request.method == 'GET':
            keywords = request.GET.get('keywords')
            result = Product.objects.filter(title__icontains=keywords)

            context = {
                'result': result,
                'keywords': keywords
            }
            return render(request, 'search.html', context)
    except Exception as e:
        print(e)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol xato!")
            return redirect('login')
    return render(request, 'registration/login.html')


def register_view(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')

            try:
                User.objects.get(username=username)
                messages.error(request, "Foydalanuvchi nomi allaqachon mavjud!")
            except User.DoesNotExist:
                user = User()
                user.first_name = request.POST.get('first_name')
                user.last_name = request.POST.get('last_name')
                user.username = request.POST.get('username')
                user.phone = request.POST.get('phone')
                password1 = request.POST.get('password1')
                password2 = request.POST.get('password2')

                if password1 == password2:
                    user.password = password1
                    user.save()
                    messages.success(request,
                                     "Muvoffaqiyatli ro'yxatdan o'tildi! Endi Ro'yxatdan o'tgan Foydalanuvchi nomingiz va parolingizni kiriting.")
                    return redirect('login')
                else:
                    messages.error(request, "Parolni to'g'ri kiriting!")

        except Exception as e:
            print(e)
            messages.error(request, 'Foydalanuvchi nomi yoki parol xato')
    return render(request, 'registration/register.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def to_session(request, id):
    if request.method == 'POST':
        quantity = request.POST.get('product_quantity')
        size = request.POST.get('product_size')
        color = request.POST.get('product_color')

        return redirect('buy-one-product', id, quantity, size, color)


def buy_one_product(request, id, quantity, size, color):
    product = Product.objects.get(id=id)
    total_price = int(product.price) * int(quantity)

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

        order_item = OrderItem()
        order_item.product = product
        order_item.order = order

        order_item.title = product.title
        order_item.image = product.image
        order_item.price = product.price
        order_item.quantity = quantity
        order_item.color = color
        order_item.size = size
        order_item.save()

        return redirect('success-page')

    context = {
        'product': product,
        'quantity': quantity,
        'size': size,
        'color': color,
        'total_price': total_price
    }

    return render(request, 'buy_one_product.html', context)
