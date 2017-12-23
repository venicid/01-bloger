from django.shortcuts import render,HttpResponse,redirect
from firstapp.models import People,Aritcle,Comment
from django.template import Context,Template
from firstapp.form import CommentForm



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

def detail(request):
    """创建评论视图"""
    if request.method == 'GET':
        form = CommentForm() #实例化一个表单
    if request.method == 'POST':
        form = CommentForm(request.POST)  #提交数据
        print(form)

        if form.is_valid():       #判断表单的数据是否通过验证;
            print(form.is_valid)  #返回布尔值,True 或者False
            print(form.cleaned_data)
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name,comment=comment)  #把数据储存到Comment模型的实例c中
            c.save()  #保存到数据库
            return redirect(to='detail')


    context ={}
    comment_list = Comment.objects.all()   #获取comment评论的所有数据
    context['comment_list'] = comment_list

    context['form'] = form
    print('11111')
    print(form.errors)
    print('2222')
    print(form)

    comment_page = render(request,'article-detail.html',context)  #render函数
    return comment_page
