from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _  # import translator

from .models import BlogPost

class CreateBlogPostModelForm(ModelForm):

    class Meta:
        model = BlogPost
        # fields = '__all__'   # Bad Approach
        fields = ['title', 'body']  # Good approach

        # added in Bounus section of part II

        # form renames title to heading but in the model
        # it remains title
        labels = {'title': _('Heading')}  

        # add help texts for title and body
        help_texts = {
            'title': _('Give your blog post a suitable heading'),
            'body': _('Write the content of the blog')
        }

