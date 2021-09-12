from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import date
from django.template.loader import render_to_string

# Create your views here.

all_posts = [
    {
        "slug":"hike-in-the-mountains",
        "image":"mountains.jpg",
        "author":"Pedro",
        "date": date(2021, 8, 29),
        "title":"Mountain Hiking",
        "excerpt":"There's nothing like the views you get when hiking the moutains! I wasn't even prepare!",
        "content":"""
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            """
    },
    
    {
        "slug":"programming-is-fun",
        "image":"coding.jpg",
        "author":"Pedro",
        "date": date(2021, 7, 21),
        "title":"Programming is Great!",
        "excerpt":"Did you ever spent hours searching that one error in your code?",
        "content":"""
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            """
    },
    
    {
        "slug":"into-the-woods",
        "image":"woods.jpg",
        "author":"Pedro",
        "date": date(2021, 3, 16),
        "title":"Nature At Its Best!",
        "excerpt":"Nature is amazing! The amount of inspiration I get when walking in the nature is incredible!",
        "content":"""
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            
                    Lorem, ipsum dolor sit amet consectetur adipisicing elit. Adipisci, a quas. Architecto totam dolor, 
            corporis at culpa officia quisquam illo 
            quis voluptatem fugiat saepe neque vero ut a doloremque quia!
            """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts":latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })

def post_detail(request, slug):
    try:
        identified_post = next(post for post in all_posts if post['slug']==slug)
        return render(request, "blog/post-detail.html", {
            "post":identified_post
        })
    except:
        response_data= render_to_string("404.html")
        return HttpResponseNotFound(response_data)