from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
  class Meta:
    model = Tweet
    fields = ['text', 'photo']
    