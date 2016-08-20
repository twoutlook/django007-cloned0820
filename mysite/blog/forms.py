from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'brief',
        'r03c3','r03c4','r03c5','r03c6','r03c7',
        )