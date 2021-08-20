from django.shortcuts import render



posts = [
    {
        'author': 'mike',
        'title': 'troof',
        'content': 'da troofsad',
        'date_posted': 'da troofday'
    },
    {
        'author': 'dyke',
        'title': 'troof',
        'content': 'da astroof',
        'date_posted': 'asda tadsroofday'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'mainapp/home.html', context)

def about(request):
    return render(request, 'mainapp/about.html')
