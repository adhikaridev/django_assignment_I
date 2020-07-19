from django.http import HttpResponse
from django.template import loader
from .models import Blog, Author


def home(request):
    context = {}
    template = loader.get_template('home.html')
    template_data = template.render(context, request)
    return HttpResponse(template_data)


def all_blogs(request):
    blog_qs = Blog.objects.all()
    blog_and_authors = {}
    for blog in blog_qs:                # blog is an object/row
        author_qs = blog.author.all()     # author_qs is a query set
        author_list = []
        for author in author_qs:
            author_list.append(author.name)
        blog_and_authors[blog] = author_list
    context = {'blog_and_authors': blog_and_authors}    # blog_and_authors is a dictionary
    template = loader.get_template('blogs.html')
    template_data = template.render(context, request)
    return HttpResponse(template_data)


def all_authors(request):
    author_qs = Author.objects.all()
    context = {'authors': author_qs}
    template = loader.get_template('authors.html')
    template_data = template.render(context, request)
    return HttpResponse(template_data)

