from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=4)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'title'
        ]

    def clean_text(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == text:
            raise ValidationError(
            "Заголовок не должен быть идентичным тексту."
            )
        if title[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )
        return text
