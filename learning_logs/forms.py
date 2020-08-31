from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        """Build from from the Topic model"""
        model= Topic
        fields = ['text']
        """django does not generate a label for text field"""
        labels ={'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
