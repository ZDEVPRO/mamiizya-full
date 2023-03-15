from site_settings.models import *
from Sections.models import *
from home.models import *
from shopcart.models import *


def settings(request):
    contact = ContactData.objects.last()
    category = Category.objects.all()

    section1 = Section1.objects.last()
    section2 = Section2.objects.last()
    section3 = Section3.objects.last()
    section4 = Section4.objects.last()

    if request.user.is_authenticated:
        cart_items_count = ShopCart.objects.filter(user=request.user).count()
    else:
        cart_items_count = 0

    context = {
        'contact': contact,
        'category': category,
        'cart_items_count': cart_items_count,

        'section1': section1,
        'section2': section2,
        'section3': section3,
        'section4': section4
    }
    return context
