from django.shortcuts import render

from datetime import datetime

def blog_details(request):
    post = {
        "title": "my first python title",
        "descriptions" : "Dejango is high level programming language",
        "author": None,
        "created_at": datetime.now(),
        "comments_count": 5,
        "tags": ["Django","Python","java"],
        "price": 100,
        "number": 7,
    }
    return render(request,'blog/blog_details.html',{"post":post})
