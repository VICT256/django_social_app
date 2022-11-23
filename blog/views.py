from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from common.decorators import ajax_required
from .forms import CommentForm, PostForm
from .models import Post


@login_required
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST, files=request.FILES)
        if post_form.is_valid():
            pf = post_form.save(commit=False)
            pf.author = request.user
            pf.save()
            messages.success(request, 'Your post created successfully')
            return redirect('home')
    else:
        post_form = PostForm()
    return render(request, 'blog/create-post.html', {'post_form': post_form})


@require_POST
@ajax_required
@login_required
def users_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try: 
            post = Post.objects.get(id=post_id)
            if action == "like":
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})
                

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            cf = comment_form.save(commit=False)
            cf.post = post
            cf.author = request.user
            cf.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post-detail.html', {'post': post, 'comment_form': comment_form})