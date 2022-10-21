from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.


def index(request):
    articles = Review.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


# def new(request):
#     article_form = ReviewForm()
#     context = {
#         'review_form' : article_form
#     }
#     return render(request, 'articles/new.html',context=context)


def create(request):
    if request.method == "POST":
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # movie_name = request.POST.get('movie_name')
        # grade = request.POST.get('grade')
        # created_at = request.POST.get('created_at')
        # updated_at = request.POST.get('updated_at')
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect("articles:index")
    else:
        article_form = ReviewForm()
    context = {"review_form": article_form}
    return render(request, "articles/new.html", context=context)
    # Review.objects.create(title=title, content=content, movie_name=movie_name, grade=grade, created_at=created_at, updated_at=updated_at)


def detail(request, pk):
    article = Review.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=article)
        if review_form.is_valid():
            review_form.save()
        return redirect("articles:detail", article.pk)
    else:
        review_form = ReviewForm(instance=article)

    context = {"review_form": review_form}
    return render(request, "articles/update.html", context)


def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("articles:index")


def articles(request):
    articles = Review.objects.order_by("-pk")
    context = {"articles": articles}
    return render(request, "articles/articles.html", context)
