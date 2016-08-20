from django import forms
from .models import Spec

# from .models import Post

# class PostForm(forms.ModelForm):

#     class Meta:
#         model = Post
#         fields = ('title', 'text',)
    #      field1 = models.IntegerField()
    # field2 = models.CharField(max_length=200,verbose_name="規格說明")
    # field3 = models.CharField(max_length=200,null=True)
  
class SpecForm(forms.ModelForm):

    class Meta:
        model = Spec
        fields = ('field1', 'field2','field3',)        