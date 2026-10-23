from django.shortcuts import render

from datetime import datetime

def blog_list(request):
    blogs = [
        {"title":"Django Basics", "is_featured":True, "author": "john Doe"},
        {"title":"Django Advance", "is_featured":False, "author": ""},
        {"title":"Django Rest framework", "is_featured":False, "author": "john"},
    ]
    context = {
        "blogs": blogs,
        "today": datetime.now(),
        "html_code":"<h1>welcome to my blog </h1>",
    }
    return render(request,'blog/blog_list.html',context)
