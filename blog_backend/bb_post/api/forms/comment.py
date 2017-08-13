from django import forms
from bb_post.models import Post


class CreateForm(forms.Form):

    post = forms.ModelMultipleChoiceField(queryset=Post.objects.all())
    content = forms.CharField()
