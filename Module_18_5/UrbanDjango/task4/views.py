from lib2to3.fixes.fix_input import context

from django.shortcuts import render


def main_page(request):
    title = 'Магазин Свежесть'
    main_head = ('Главная страница магазин "Свежесть"')
    main_comment = 'На нашем сайте вы всегда можете купить свежие и вкусные овощи и фрукты'

    context={
        'title':title,
        'main_head': main_head,
        'main_comment': main_comment,
    }
    return render(request, 'fourth_task/main.html',context)


def market_page(request):
    title = 'Магазин Свежесть'
    market_head = 'Наша витрина'
    context={
        'title': title,
        'market_head':market_head,
        'products':['Апельсины','Бананы','Яблоки','Огурцы','Помидоры','Баклажаны'],
    }
    return render(request, 'fourth_task/market.html',context)


def basket_page(request):
    title = 'Магазин Свежесть'
    basket_head = 'Сейчас в Вашей корзине'
    context={
        'title': title,
        'basket_head': basket_head,
        'choice_list':['Апельсины 1 кг','Бананы 1 кг','Помидоры 2 кг','Баклажаны 1 кг']
    }
    return render(request, 'fourth_task/basket.html',context)
# Create your views here.
