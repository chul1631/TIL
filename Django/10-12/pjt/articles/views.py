from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.

# 요청 정보를 받아서..
def index(request):
    articles = Article.objects.order_by("-pk")
    # template 에 뿌려준다
    context = {"articles": articles}
    return render(request, "articles/index.html", context)


def create(request):
    if request.method == "POST":
        # DB에 저장하는 로직
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect("articles:index")
    else:
        article_form = ArticleForm()
    context = {"article_form": article_form}
    return render(request, "articles/new.html", context=context)


def detail(request, pk):
    # 특정 글을 가져온다.
    #                        .get(모델칼럼명=urls.py에서 쓴 인자)
    article = Article.objects.get(pk=pk)
    # template 에 객체 전달
    context = {"article": article}
    return render(request, "articles/detail.html", context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "POST":
        # POST : input 가져와서 검증하고 DB 에 저장
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            # 유효성 검사 통과하면 저장후 상세보기 페이지로
            article_form.save()
            return redirect("articles:detail", article.pk)
        # 유효성 검사 통과 못하면 => 오류메세지
    else:
        # GET 처리 : Form 을 제공
        article_form = ArticleForm(instance=article)
    context = {"article_form": article_form}
    return render(request, "articles/update.html", context)


def delete(request, pk):
    Article.objects.get(pk=pk).delete()
    return redirect("articles:index")
