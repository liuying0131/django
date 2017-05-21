#coding:utf-8
from django import forms
from .models import *


class StuForm(forms.ModelForm):
    class Meta:
        model = Student  # 基于模型的表单
        exclude = []  # uncomment this line and specify any field to exclude it from the form

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade  # 基于模型的表单
        exclude = []  # uncomment this line and specify any field to exclude it from the form


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review  # 基于模型的表单
        exclude = []  # uncomment this line and specify any field to exclude it from the form

