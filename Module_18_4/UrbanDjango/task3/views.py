from lib2to3.fixes.fix_input import context

from django.shortcuts import render


def main_page(request):
    title = 'Магазин Свежесть'
    main_head = ('Главная страница магазин "Свежесть"')
    main_comment = 'На нашем сайте вы всегда можете купить свежие и вкусные овощи и фрукты'
    chapter_1 = 'Главная'
    chapter_2 = 'Магазин'
    chapter_3 = 'Корзина'
    context={
        'title':title,
        'main_head': main_head,
        'main_comment': main_comment,
        'chapter_1':chapter_1,
        'chapter_2':chapter_2,
        'chapter_3':chapter_3
    }
    return render(request, 'third_task/main.html',context)


def market_page(request):
    title = 'Магазин Свежесть'
    market_head = 'Наша витрина'
    fruit_1='Апельсины'
    fruit_2='Бананы'
    fruit_3='Яблоки'
    veget_1='Огурцы'
    veget_2='Помидоры'
    veget_3='Баклажаны'
    context={
        'title':title,
        'market_head':market_head,
        'fruit_1':fruit_1,
        'fruit_2':fruit_2,
        'fruit_3':fruit_3,
        'veget_1':veget_1,
        'veget_2':veget_2,
        'veget_3':veget_3
    }
    return render(request, 'third_task/market.html',context)


def basket_page(request):
    title = 'Магазин Свежесть'
    basket_head = 'Сейчас в Вашей корзине'
    choice_1='Апельсины 1 кг'
    choice_2='Бананы 1 кг'
    choice_3='Помидоры 2 кг'
    choice_4='Баклажаны 1 кг'
    context={
        'title': title,
        'basket_head': basket_head,
        'choice_1':choice_1,
        'choice_2':choice_2,
        'choice_3':choice_3,
        'choice_4':choice_4
    }
    return render(request, 'third_task/basket.html',context)
# Create your views here.
