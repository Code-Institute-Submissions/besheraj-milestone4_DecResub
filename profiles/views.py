from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.conf import settings

from checkout.models import Order


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile' : profile
    }
    return render(request, template, context)



@login_required
def update_profile(request):
    # Display the user's profile.
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')        
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    template = 'profiles/update_profile.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def order_history(request, order_number):
    # display the order receipt
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'total': settings.PRICE

    }
    return render(request, template, context)


@login_required
def order_history_table(request):
    # display the order history
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
        'on_profile_page': True,
    }
    return render(request, template, context)


@login_required
def available_quizes(request):
    profile = UserProfile.objects.get(user=request.user)
    orders = Order.objects.filter(user_profile=profile, status="paid")
    context = {
        'orders': orders,
    }
    return render(request, 'profiles/available_quizes.html', context)
