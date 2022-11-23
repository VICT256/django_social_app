from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        fields = ['title', 'content', 'image',]


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Write Your Comment Here"}))

    class Meta:
        model = Comment
        fields = ['content']