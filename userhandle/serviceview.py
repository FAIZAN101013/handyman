from django.db.models import Q
from django.http import HttpResponseRedirect
from .models import HandymanUser
from django.shortcuts import render, redirect
from django.urls import path
from functools import wraps


# Handymen (FixR) should never see the customer-facing browse/booking pages —
# send them to their dashboard instead.
def customer_only(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_FixR:
            return redirect('index')
        return view(request, *args, **kwargs)
    return wrapper


# A handyman turns up for a service either because it is their headline service
# or because they added it as one of their job profiles. distinct() matters:
# joining across offerings would otherwise repeat a handyman once per match.
def handymen_for(service):
    return HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        Q(handyman_services__contains=service) | Q(offerings__service=service),
    ).exclude(
        Q(handyman_services="All Services") & Q(offerings__isnull=True)
    ).distinct()


# Handymen who cover everything. Since handyman_services defaults to
# "All Services" and is no longer editable, the legacy field alone would sweep
# in every profile that never configured anything -- a set price is what marks
# a legacy profile as deliberately set up.
def all_round_handymen():
    return HandymanUser.objects.filter(
        Q(is_customer=False),
        Q(is_superuser=False),
    ).filter(
        Q(offerings__service="All Services")
        | (
            Q(offerings__isnull=True)
            & Q(handyman_services="All Services")
            & Q(price__isnull=False)
        )
    ).distinct()


@customer_only
def General(request):
    allservicelist = all_round_handymen()
    services = handymen_for("General Handyman")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)




@customer_only
def Furniture(request):
    allservicelist = all_round_handymen()
                        
                       
                    
    services = handymen_for("Furniture Assembly")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def Moving(request):
    allservicelist = all_round_handymen()
    services = handymen_for("Help Moving")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def Mounting(request):
    allservicelist = all_round_handymen()

    services = handymen_for("TV Mounting")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)
    

@customer_only
def Painting(request):
    allservicelist = all_round_handymen()

    services = handymen_for("Painting")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


    
@customer_only
def disinfecting_services(request):
    allservicelist = all_round_handymen() 
    services = handymen_for("Disinfecting Services")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)





@customer_only
def ikea_services(request):
    allservicelist = all_round_handymen() 
    services = handymen_for("IKEA Services")
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def all_services(request):
    
    services = HandymanUser.objects.all().filter(is_superuser=False).exclude(is_customer=True)
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


#  adding the filtering urls and requests here 



# Price filters match on the headline rate or on any job profile's rate, so a
# handyman who charges £8 for one job still shows under the cheapest bracket.
def handymen_priced(low=None, high=None):
    base, offering = Q(), Q()
    if low is not None:
        base &= Q(price__gte=low)
        offering &= Q(offerings__price__gte=low)
    if high is not None:
        base &= Q(price__lte=high)
        offering &= Q(offerings__price__lte=high)
    return HandymanUser.objects.filter(
        Q(is_FixR=True), Q(is_customer=False), Q(is_superuser=False),
    ).filter(base | offering).distinct()


@customer_only
def lowpricehandyman(request):
    services = handymen_priced(high=10)
    allservicelist = ''
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)



@customer_only
def highpricehandyman(request):
    services = handymen_priced(low=50)
    allservicelist = ''
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)



@customer_only
def mediumpricehandyman(request):
    services = handymen_priced(low=10, high=50)
    allservicelist = ''
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)



@customer_only
def lowratinghandyman(request):
    services = HandymanUser.objects.all().filter(
        Q(is_FixR=True) & Q(is_customer=False) & 
        Q(is_superuser=False) & Q(handyman_rating__lte=2)
    )
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}

    return render(request, 'search_result.html', context)


@customer_only
def mediumratinghandyman(request):
    services = HandymanUser.objects.all().filter(
        Q(is_FixR=True) & Q(is_customer=False) & 
        Q(is_superuser=False) & Q(handyman_rating__gte=2) 
        & Q(handyman_rating__lte=3.5)
    )
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def highratinghandyman(request):
    services = HandymanUser.objects.all().filter(
        Q(is_FixR=True) & Q(is_customer=False) & 
        Q(is_superuser=False) & Q(handyman_rating__gte=3.5)
    )
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)












serviceurlpattern = [
    path('contactless-task/', General, name='general-handyman' ),
    path('furnitureassembly/', Furniture, name='furniture-assembly' ),
    path('painting/', Painting, name='painting' ),
    path('tvmounting/', Mounting, name='tv-mounting' ),
    path('disinfecting-services/', disinfecting_services, name='disinfecting-services' ),
    path('help-moving/', Moving, name='help-moving' ),
    path('IKEA-services/', ikea_services, name='ikea-services' ),
    path('all-services/', all_services, name='all-services' ),
    path('lowest-priced-handyman/', lowpricehandyman, name='low-price'),
    path('highest-priced-handyman/', highpricehandyman, name='high-price'),
    path('medium-priced-handyman/', mediumpricehandyman, name='medium-price'),
    path('lowest-rated-handyman/', lowratinghandyman, name='low-rating'),
    path('medium-rated-handyman/', mediumratinghandyman, name='medium-rating'),
    path('highest-rated-handyman/', highratinghandyman, name='high-rating'),






    

]