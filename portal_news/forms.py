from django import forms
from django.forms import ModelForm, HiddenInput, CharField, Textarea
from .models import Post
from .models import Author
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
#news/create
class PostForm(ModelForm):
    author = forms.ModelChoiceField(
        label='Автор',
        queryset=Author.objects.order_by('-user').all(),
        empty_label='Выберите автора',
    )
    heading_post = CharField(label='Название - заголовок')
    text_post = CharField(label='Текст', widget=Textarea)

    class Meta:
        model = Post
        fields = ['heading_post', 'select_choices', 'category', 'text_post', 'author']
        widgets = {
            'author': HiddenInput(),
        }

    class CommonSignupForm(SignupForm):
        def save(self, request):
            user = super(CommonSignupForm, self).save(request)
            common_group = Group.objects.get(name='common')
            common_group.user_set.add(user)
            return user
