from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text', 'language',)
        labels = {
            'text': _(''),
            'language': _(''),
        }
