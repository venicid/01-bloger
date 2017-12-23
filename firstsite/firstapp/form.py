from django import forms
from django.core.exceptions import ValidationError

# Create your views here.

def words_validator(comment):
    if len(comment) < 4:
        raise ValidationError('内容不足4个字符')  #当comment不足4个字符，升起一个错误

def comment_validator(comment):
    if 'a' in comment:
        raise ValidationError('不能包含a字符')

class CommentForm(forms.Form):
    """定义一个Django自带的表单类"""
    name = forms.CharField(max_length=50)
    comment = forms.CharField(
        widget=forms.Textarea(),  #comment 表单的类型为Textarea
        error_messages = { 'required':'请输入内容'},  #error_messages报错信息
        validators = [words_validator,comment_validator],  #验证器参数
        )
