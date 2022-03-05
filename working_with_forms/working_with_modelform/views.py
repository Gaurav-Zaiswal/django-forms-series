from django.forms import ValidationError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CreateBlogPostModelForm
from .models import BlogPost # imported this

# Create your views here.
def create_blog_view(request):
    """
    check if it is a POST request. If it is a post request
    then populate the form and check if the form is valid or not, if form is valid then
    directly save() the form, for any request method other than POST re-render the blank
    form.
    """
    if request.method == "POST":
        form = CreateBlogPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-posts')
            
        # comment down below two lines of code, as we are not overriding the validation message here
        # else:
        #     raise ValidationError("Invalid form")
    else:
        form = CreateBlogPostModelForm()
    
    return render(request, "create_blog_post.html", {'form': form})


def get_blog_posts_list_view(request):
    """
    get the listing of id, title of all the availabe posts
    """

    # posts = BlogPost.objects.all() # not an efficient code

    # fetch titles, and ids only
    posts = BlogPost.objects.all().values('id', 'title')       
    return render(request, 'homepage.html', {'posts': posts})


def get_detailed_blog_post(request, id):
    """
    get the detailed post
    """
    if request.method == 'GET':
        # post = BlogPost.objects.get(id=id)

        # raise 404 if the post with id does not exist
        post = get_object_or_404(BlogPost, id=id)  # recommended 

        return render(request, 'detailedpage.html', {'post': post} )
