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
    print(request)
    print("==="*30)
    print(dir(request))
    print("==="*30)
    print(type(request))

    queryset = request.GET.get('tag')
    print(queryset)

    if queryset:
        article_list = Aritcle.objects.filter(tag=queryset)  #过滤器
    else:
        article_list = Aritcle.objects.all()  #获取Article数据库所有的数据

    context = {}
    context['article_list'] = article_list
    index_page = render(request,'firstweb.html',context)
    return index_page


def detail(request, page_num, error_form=None):
    """加载文章，评论视图"""
    context ={}
    form = CommentForm
    a = Aritcle.objects.get(id=page_num)      #最优评论  #查找出该文章的id号
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)  #best_comment返回的是list列表
                                                                        #select *from where best_comment=True and belong_to=a
    if best_comment:
        context['best_comment'] = best_comment[0]
    article = Aritcle.objects.get(id=page_num)  #取出id为page_num这篇文章
    context['article'] = article

    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = form

    comment_page = render(request,'article-detail.html',context)  #render函数
    return comment_page

def detail_comment(request, page_num):
    """post方法form表单提交"""
    form = CommentForm(request.POST)  #提交数据
    print(form)
    if form.is_valid():       #判断表单的数据是否通过验证;
                                            #print(form.is_valid)  #返回布尔值,True 或者False
                                            #print(form.cleaned_data)
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        a = Aritcle.objects.get(id=page_num)      #查找出该文章的id号
        c = Comment(name=name,comment=comment, belong_to=a)  #把数据储存到Comment模型的实例c中
        c.save()  #保存到数据库
    else:
        return detail(request, page_num, error_form=form)
    return redirect(to='detail', page_num=page_num)

#
# def detail(request,page_num):
#     """创建评论视图"""
#     if request.method == 'GET':
#         form = CommentForm() #实例化一个表单
#     if request.method == 'POST':
#         form = CommentForm(request.POST)  #提交数据
#         print(form)
#         if form.is_valid():       #判断表单的数据是否通过验证;
#             print(form.is_valid)  #返回布尔值,True 或者False
#             print(form.cleaned_data)
#             name = form.cleaned_data['name']
#             comment = form.cleaned_data['comment']
#             a = Aritcle.objects.get(id=page_num)      #查找出该文章的id号
#             c = Comment(name=name,comment=comment, belong_to=a)  #把数据储存到Comment模型的实例c中
#             c.save()  #保存到数据库
#             return redirect(to='detail', page_num=page_num)



    #comment_list = Comment.objects.all()   #获取comment评论的所有数据

    #context['comment_list'] = comment_list

    # print('11111')  for testing
    # print(form.errors)
    # print('2222')
    # print(form)
