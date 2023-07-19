from django import forms
from ps.models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostForm(forms.Form):
    author = forms.CharField(max_length=30)
    head = forms.Textarea()
    text = forms.CharField(max_length=30)
    page_layk = forms.IntegerField()