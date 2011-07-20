from django import forms

class CreateBookmarkForm(forms.Form):
    post_id = forms.CharField()
