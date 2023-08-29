from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # title = forms.CharField(
    #     label='제목 입력창',
    #     widget=forms.TextInput(
    #         attrs = {'class': 'form-control'}
    #     )
    # )


    class Meta:
        model = Article
        # fields = ('title','content')
        exclude = ('user',)
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'})
        # }