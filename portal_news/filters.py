from django_filters import FilterSet, DateFilter, CharFilter
from .models import Post, Author
from django import forms

class PostFilter(FilterSet):
    time = DateFilter(field_name="time",
                      widget=forms.DateInput(attrs={'type': 'date'}),
                      label='Дата',
                      lookup_expr='gte',
                      )
    class Meta:
        model = Post
        fields = {
            'category': ['exact'],
            'select_choices': ['exact'],
        }







