from django.http import HttpResponse
from django.shortcuts import render
from listings.choices import price_range, property_choices, state_choices

from listings.models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_range': price_range,
        'property_choices': property_choices,
        'state_choices': state_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')
