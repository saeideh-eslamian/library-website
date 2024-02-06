from django import forms

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=200, required=False)

class CommentForm(forms.Form):
    title = forms.CharField(label='Title',max_length=200)
    description = forms.CharField(label='Description',widget=forms.Textarea)
    user_name = forms.CharField(label='Name',max_length=200)
    user_email = forms.EmailField(label='Email',required=True)
  