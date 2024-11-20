from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.
def post_page(request):
    posts = Post.objects.all()
    page_size = request.GET.get('page_size', 5)
    paginator = Paginator(posts, page_size)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'page_size': page_size,
    }
    return render(request, 'post.html', context)
# Create your views here.
