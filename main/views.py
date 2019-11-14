from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def fonts(request):
    return render(request, 'main/fonts.html')


def tg_logo(request):
    return render(request, 'main/tg_logo.html')


def shop(request):
    return render(request, 'main/shop.html')


def btw_dates(request):
    return render(request, 'main/btw_dates.html')


def operations_with_matrix(request):
    return render(request, 'main/operations_with_matrix.html')
