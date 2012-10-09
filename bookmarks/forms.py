from django import forms

class CreateUserForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

class CreateBookmarkForm(forms.Form):
    post_id = forms.CharField()
    thread_title = forms.CharField()
