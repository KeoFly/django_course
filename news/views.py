from django.shortcuts import render

from users.services import get_main_news, get_news_list


def index(request):
    main_news = get_main_news()
    news_list = get_news_list([main_news])
    context = dict(main_news=main_news, news_list=news_list)
    return render(request, 'news/index.html', context=context)
