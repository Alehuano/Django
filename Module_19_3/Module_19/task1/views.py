from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from .models import Buyer, Game


# users = ['Alex', 'Serg', 'Ilya']


def main_page(request):
    title = 'Магазин Игромания'
    main_head = ('Главная страница магазин "Игромания"')
    main_comment = 'На нашем сайте вы всегда можете приобрести самые интересные игры'

    context = {
        'title': title,
        'main_head': main_head,
        'main_comment': main_comment,
    }
    return render(request, 'main.html', context)


def market_page(request):
    title = 'Магазин Buhjvfybz'
    market_head = 'Наша витрина'
    games_db = Game.objects.all()
    context = {
        'title': title,
        'market_head': market_head,
        'games_db': games_db,
    }
    return render(request, 'market.html', context)


def basket_page(request):
    title = 'Магазин Игромания'
    basket_head = 'Сейчас в Вашей корзине'
    games_db=Game.objects.all()
    context = {
        'title':title,
        'basket_head':basket_head,
        'games_db':games_db,
    }
    return render(request, 'basket.html', context)


def sign_up_by_django(request):
    info = {}

    users_db = Buyer.objects.values_list('name', flat=True)

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username not in users_db and password == repeat_password and age >= 18:
                Buyer.objects.create(name=username, age=age, balance=500)
                return HttpResponse(f'Приветствуем, {username}')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users_db:
                info['error'] = f'Пользователь {username} уже существует'
        else:
            form = UserRegister()

    return render(request, 'registration_page.html', info)

# Create your views here.
