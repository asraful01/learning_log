from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        """Build from from the Topic model"""
        model= Topic
        fields = ['text']
        """django does not generate a label for text field"""
        labels ={'text':''}
