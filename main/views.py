from django.shortcuts import render


def main(request):
    return render(request, 'main/main.html')


def fonts(request):
    return render(request, 'main/fonts.html')

def tg_logo(request):
    return render(request, 'main/tg_logo.html')

def shop(request):
    return render(request, 'main/shop.html')
