# Creating views here.

from django.shortcuts import render, redirect
from .models import BloodPost
from .forms import BloodForm
from django.db.models import Q  # add this at the top with imports
from django.shortcuts import get_object_or_404

def home(request):
    query = request.GET.get('q', '')  # search query
    posts = BloodPost.objects.all().order_by('-created_at')
    
    if query:
        posts = posts.filter(
            Q(blood_type__icontains=query) | Q(city__icontains=query)
        )

    return render(request, "home.html", {"posts": posts, "query": query})


def create_post(request):
    if request.method == 'POST':
        form = BloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BloodForm()
    return render(request, 'create_post.html', {'form': form})


def help_page(request):
    return render(request, 'help.html')

def about(request):
    return render(request, "about.html")


def delete_post(request, id):
    post = get_object_or_404(BloodPost, id=id)
    post.delete()
    return redirect('home')



