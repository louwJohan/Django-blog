# from .models import Comment
# from django import forms


# class CommentForm(forms.Modelform):
#     class Meta:
#         model = Comment 
#         fields = ('body',)

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)