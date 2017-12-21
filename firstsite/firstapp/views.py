from django.shortcuts import render,HttpResponse
from firstapp.models import People,Aritcle
from django.template import Context,Template
# Create your views here.

def first_try(request):
    person = People(name='alxe',job='it')
    html_string = '''
                <!DOCTYPE html>
                <html>
                  <head>
                    <meta charset="utf-8">
                    <title>first_try</title>
                  </head>
                  <body>
                    <h1>Hello</h1>
                    <h3> {{ person.name }} </h3>
                  </body>
                </html>
    '''
    t = Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)

    return HttpResponse(web_page)


def index(request):
    context = {}
    article_list = Aritcle.objects.all()  #获取Article数据库所有的数据
    context['article_list'] = article_list
    index_page = render(request,'firstweb.html',context)
    return index_page
