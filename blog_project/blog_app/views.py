from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from rest_framework import viewsets
from .serializers import PostSerializer

# Home page displaying all posts
def index(request):
    posts = Post.objects.all()
    return render(request, 'blog_app/index.html', {'posts': posts})

# Post detail view
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_app/post_detail.html', {'post': post})

# Create new post (only accessible to logged-in users)
@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog_app/post_create.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})
# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
            # form = form.save(commit=False)
            # form.author = request.user
            # form.save()
#             form.save()
#             return redirect('index')  # Redirect to a success page or home page
#     else:
#         form = PostForm()

#     return render(request, 'blog_app/post_create.html', {'form': form})


# Edit an existing post
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/post_edit.html', {'form': form})

# Delete a post
# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == "POST":
#         post.delete()
#         return redirect('index')
#     return render(request, 'blog_app/post_delete.html', {'post': post})
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # Check if the logged-in user is the author of the post
    if post.author != request.user:
        return redirect('post_list')  # Redirect if the user is not the post's author

    if request.method == "POST":
        post.delete()
        return redirect('post_list')  # Redirect to the post list after deletion
    
    return render(request, 'blog_app/post_delete.html', {'post': post})

def logout_success(request):
    return render(request, 'blog_app/logout.html')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer