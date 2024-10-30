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


@customer_only
def General(request):
    allservicelist = HandymanUser.objects.filter(
            Q(is_superuser=False),
            Q(is_customer=False),
            
            Q(handyman_services="All Services")
            )
    services = HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        handyman_services__contains= "General Handyman"
        ).exclude(
     
        Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)




@customer_only
def Furniture(request):
    allservicelist = HandymanUser.objects.filter(
            Q(is_superuser=False),
            Q(is_customer=False),
           
            Q(handyman_services="All Services")
            )
                        
                       
                    
    services = HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        handyman_services__contains= "Furniture Assembly"
        ).exclude(

         
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def Moving(request):
    allservicelist = HandymanUser.objects.filter(
            Q(is_superuser=False),
            Q(is_customer=False),
           
            Q(handyman_services="All Services")
            )
    services = HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        handyman_services__contains= "Help Moving"
        ).exclude(
       
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def Mounting(request):
    allservicelist = HandymanUser.objects.filter(
            Q(is_superuser=False),
            Q(is_customer=False),
           
            Q(handyman_services="All Services")
            )

    services = HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        handyman_services__contains= "Tv Mounting"
        ).exclude(
         
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)
    

@customer_only
def Painting(request):
    allservicelist = HandymanUser.objects.filter(
            Q(is_superuser=False),
            Q(is_customer=False),
           
            Q(handyman_services="All Services")
            )

    # services = HandymanUser.objects.all().filter(handyman_services__contains='painting' ,is_superuser=False).exclude(is_customer=True)
    services = HandymanUser.objects.filter(
        Q(is_superuser=False),
        Q(is_customer=False),
        Q(handyman_services__contains= "Painting")

        ).exclude(
        
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


    
@customer_only
def disinfecting_services(request):
    allservicelist = HandymanUser.objects.filter(
          
            Q(handyman_services="All Services")
            ).exclude(
                        Q(is_customer=True)|
                        Q(is_superuser=True)
                       
                        ) 
    services = HandymanUser.objects.filter(
        handyman_services__contains= "Disinfecting Services"
        ).exclude(
          
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)





@customer_only
def ikea_services(request):
    allservicelist = HandymanUser.objects.filter(
            Q(handyman_services="All Services")& 
            Q(is_FixR=True) & Q(is_customer=False) & Q(is_superuser=False)
            ).exclude(
                        Q(is_customer=True)|
                        Q(is_superuser=True)
                       
                        ) 
    services = HandymanUser.objects.filter(
        handyman_services__contains= "IKEA"
        ).exclude(
            Q(handyman_services="All Services")  
        )
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


@customer_only
def all_services(request):
    
    services = HandymanUser.objects.all().filter(is_superuser=False).exclude(is_customer=True)
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)


#  adding the filtering urls and requests here 



@customer_only
def lowpricehandyman(request):
    services = HandymanUser.objects.filter(price__lte=10)
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)



@customer_only
def highpricehandyman(request):
    services = HandymanUser.objects.filter(price__gte=50)
    allservicelist = '' 
    context = {'servicelist':services, 'allservicelist': allservicelist}
    return render(request, 'search_result.html', context)



@customer_only
def mediumpricehandyman(request):
    services = HandymanUser.objects.all().filter(
        Q(price__gte=10)& Q(price__lte=50)& Q(is_FixR=True) & Q(is_customer=False) & 
        Q(is_superuser=False))
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