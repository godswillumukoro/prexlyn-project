from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

from listings.choices import price_range, property_choices, state_choices

from django.http import Http404


from .models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def property_choice(request, property_type):
    if property_type == 'apartment':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    elif property_type == 'bungalow':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    elif property_type == 'duplex':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    elif property_type == 'land':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    elif property_type == 'cottage':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    elif property_type == 'house':
        queryset_list = Listing.objects.filter(
            property_choice__icontains=property_type)
    else:
        raise Http404("Page not found")

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/property-choice.html', context)


def search(request):

    queryset_list = Listing.objects.order_by('list_date')  # Get all items
    # price_range = {
    #     'sugar': 'pudding'
    # }

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(title__icontains=keywords)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__icontains=state)

    if 'property_choice' in request.GET:
        property_choice = request.GET['property_choice']
        if property_choice:
            queryset_list = queryset_list.filter(
                property_choice__icontains=property_choice)

    if 'price_range' in request.GET:
        user_price_range = request.GET['price_range']

        if user_price_range:
            splited_value = user_price_range.split('-')
            if len(splited_value) == 2:
                queryset_list = queryset_list.filter(
                    price__lte=splited_value[1]).filter(price__gte=splited_value[0])

    paginator = Paginator(queryset_list, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': queryset_list,
        'price_range': price_range,
        'property_choices': property_choices,
        'state_choices': state_choices,
    }

    return render(request, 'listings/search.html', context)
