from django.core.exceptions import ValidationError # imported this
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _  

from .models import BlogPost


class CreateBlogPostModelForm(ModelForm):

    # added content starts
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 25:
            raise ValidationError("Heading must be 25 characters long!")

        return title
    # added content ends

    class Meta:
        model = BlogPost

        fields = ['title', 'body'] 
        labels = {'title': _('Heading')}  
        help_texts = {
            'title': _('Give your blog post a suitable heading'),
            'body': _('Write the content of the blog')
        }
