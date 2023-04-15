from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request=request, template_name="index.html", context={"number":7})

def about(request):

    return render(request=request, template_name="about.html")

def detail(request, id):

    #article = Article.objects.filter(id=id).first()

    article = get_object_or_404(Article, id=id)
    context = {
        "article":article
    }

    return render(request,"detail.html", context=context)

@login_required(login_url="user:login")
def dashboard(request):

    articles = Article.objects.filter(author=request.user)

    context = {
        "articles":articles
    }

    return render(request, "dashboard.html", context=context)

@login_required(login_url="user:login")
def addArticle(request):

    form = ArticleForm(request.POST or None, request.FILES or None)
    print(request.FILES)
    if form.is_valid():

        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale oluşturma başrılı")
        return redirect("article:dashboard")

    context = {
        "form":form
    }

    return render(request, "addarticle.html", context=context)

@login_required(login_url="user:login")
def updateArticle(request, id):
    
    article = get_object_or_404(Article, id=id)

    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request, "Makale güncelleme başrılı")
        return redirect("article:dashboard")

    context = {
        "form":form
    }

    return render(request, "update.html", context=context)

@login_required(login_url="user:login")
def deleteArticle(request, id):

    article = get_object_or_404(Article, id=id)
    article.delete()

    messages.success(request, "Makale silme başrılı")

    return redirect("article:dashboard")
    

def articles(request):

    articles = Article.objects.all()

    context = {
        "articles":articles
    }

    return render(request, "articles.html", context=context)