
from django import forms
from .models import Post , Category

# Create Forms Here

"""
    Due to migration issues, please comment the following before migrating. Once migrated, uncomment and migrate again
        - choices
        - choice_list
        - for item in choices:
            choice_list.append(item)
        - 'category' in the widgets


"""

class DateInput(forms.DateInput):
    input_type = 'date'

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('flyer', 'title', 'caption', 'location', 'category', 'event_date')
        widgets = {
            'event_date': DateInput(),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'