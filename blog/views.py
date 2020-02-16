from django.shortcuts import render

posts = [
    {
        'author' : 'ShaariqC',
        'title' : 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'August 27, 2018'
    },
    {
        'author' : 'Haaziqc',
        'title' : 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': "About"})
