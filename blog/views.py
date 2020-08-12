from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView


class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()

        return context

# def document_list(request):
#     # documents = Document.objects.all()
#
#     page = int(request.GET.get('page', 1))
#
#     paginated_by = 2
#
#     documents = get_list_or_404(Document)
#
#     total_count = len(documents)
#     total_page = math.ceil(total_count/paginated_by)




class PostListByCategory(ListView):

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

# def index(request):
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )