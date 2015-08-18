from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from  article.models import Article, Commets
# Create your views here.
def basic_one(request):
    view = "basic_one"
    html = "<html><body>This %s</body></html>" % view
    return HttpResponse(html)

def template_2(request):
    view = "template_2"
    t = get_template('1.html')
    html = t.render(Context({'name': view}))
    return HttpResponse(html)

def template_3(request):
    view = "template_3"
    return render_to_response('1.html',{'name':view})

def articles(request):
    return render_to_response('articles.html',{'articles':Article.objects.all})

def article(request, article_id=1):
    return render_to_response('article.html', {'article': Article.objects.get(id= article_id), 'comments': Commets.objects.filter(comments_article_id=article_id)})