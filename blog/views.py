from django.shortcuts import render


posts = [
    {
        'author': 'NateW',
        'title': 'Blog Post 1',
        'content': 'This is my first blog post',
        'date_posted': 'March 8, 2019'
    },
    {
    'author': 'Bob Jones',
    'title': 'Blog Post 2',
    'content': 'This is the second blog post',
    'date_posted': 'March 7, 2019'
    }


]



def home(request):
	context = {
		'posts': posts
	}

	return render(request, 'blog/home.html', context)


def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})