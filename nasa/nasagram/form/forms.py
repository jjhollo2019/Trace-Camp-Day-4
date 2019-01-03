from django import forms
from nasagram.models import NasaComment

class NasaCommentForm(forms.ModelForm):
    class Meta:
        model = NasaComment
        fields = ['comments', 'rating', 'favorite', 'date', 'image_url']
        widgets = {
            'image_url': forms.HiddenInput,
            'date': forms.HiddenInput
        }