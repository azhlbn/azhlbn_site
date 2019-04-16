from django.shortcuts import render
from placestogo.models import Place

# Create your views here.

def placestogo(request):
    places = Place.objects.all().order_by('-date')

    context = {
        'places': places,
    }

    return render(request, 'placestogo/placestogo.html', context)


def place_details(request, slug):
    place = Place.objects.get(slug=slug)
    context = {
        'place': place,
    }
    return render(request, 'placestogo/place-details.html', context)
