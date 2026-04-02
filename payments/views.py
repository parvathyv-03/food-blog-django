from django.shortcuts import render,redirect,get_object_or_404
from .models import Cart,Order
from articles.models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def add_to_cart(request,article_id):
    article = Article.objects.get(id=article_id)

    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        article=article
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def cart_view(request):
   
   cart_items = Cart.objects.filter(user=request.user)

   total = 0

   for item in cart_items:
       price = item.article.amount if item.article.amount is not None else 0
       total += price * item.quantity

   return render(request,'payments/cart.html', {
        'cart_items':cart_items,
        'total':total 
    })


def payment_success(request):
    return render(request,'payments/payment_success.html')

def increase_quantity(request,cart_id):
    cart_item = get_object_or_404(Cart,id=cart_id,user=request.user)

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

def decrease_quantity(request,cart_id):
    cart_item = get_object_or_404(Cart,id=cart_id,user=request.user)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def remove_item(request,cart_id):
     cart_item = get_object_or_404(Cart,id=cart_id,user=request.user)
     cart_item.delete()

     return redirect('cart')

def checkout_view(request):
    
    cart_items = Cart.objects.filter(user=request.user)
    total = 0

    for item in cart_items:
        if item.article.amount:
            total += item.article.amount * item.quantity

    order_id=request.session.get('order_id')

    order= Order.objects.filter(
        id=order_id,
        status='PENDING'
    ).first()

    if request.method == 'POST':
        print("POST HIT")
        print(request.POST)
    
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')

        order=Order.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            pincode=pincode
        )

        request.session['order_id']=order.id

        return redirect('payment')


    return render(request,'payments/checkout.html',{
        'cart_items':cart_items,
        'total':total,
        'order':order
    })

def payment_page(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:
        if item.article.amount:
            total += item.article.amount * item.quantity

    order_id = request.session.get('order_id')

    if request.method == 'POST':
        method = request.POST.get('method')

        if order_id:
            order = Order.objects.get(id=order_id)

            order.status = 'PAID'

            order.save()

            Cart.objects.filter(user=request.user).delete()

            del request.session['order_id']

        return redirect('payment_success')
    
    return render(request,'payments/payment.html', {
        'cart_items':cart_items,
        'total':total
    })


@login_required
def buy_now(request,article_id):
    article = Article.objects.get(id=article_id)

    cart_item,created = Cart.objects.get_or_create(
        user=request.user,
        article=article
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect ('checkout')
            