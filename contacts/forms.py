# -*- coding: utf-8 -*-
from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['subject'].widget.attrs.update(
            {
                'class': 'form-control wow fadeInDown',
                'data-wow-duration': '500ms',
                'data-wow-delay': '.6s'
            }
        )
        self.fields['sender'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})
        self.fields['copy'].widget.attrs.update({'class': 'id_copy_input'})

    class Meta:
        model = Feedback
        fields = [
            'subject',
            'sender',
            'message',
            'copy',
        ]

        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': u'Тема листа'}),
            'sender': forms.TextInput(attrs={'placeholder': u'Ваш e-mail'}),
            'message': forms.Textarea(attrs={'placeholder': u'Повідомлення', 'rows': 7})
        }
