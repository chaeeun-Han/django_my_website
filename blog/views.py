from django.shortcuts import get_object_or_404, render
from .models import Post, Category
from django.views.generic import ListView, DetailView



class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()

        return context

class PostDetail(DetailView):
    model = Post


class PostListByCategory(ListView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)

        return Post.objects.filter(category=category).order_by('-created')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()


        slug = self.kwargs['slug']
        category = Category.objects.get(slug=slug)

        return context


# def category_detail(request, slug):
#
#     category = get_object_or_404(Category, slug=slug)
#     post = Post.objects.filter(category=category)
#
#     return render(
#         request,
#         'blog/category_detail.html',
#         {
#             'category': category,
#             'post': post,
#         }
#     )


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

# def post_detail(request, pk):
#     blog_post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'blog_post': blog_post,
#          }
#     )

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