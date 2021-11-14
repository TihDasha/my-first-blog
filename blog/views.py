from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    # TODO этот фильтр бесполезен, означает "дай мне посты у которых дата публикации >= текущему моменту", таких будет 0
    #      возможно тут ожидался фильтр published_date__isnull=False чтобы отображать только опубликованные посты
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
