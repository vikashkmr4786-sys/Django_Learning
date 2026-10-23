from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def post_details(request,post_id):
    return HttpResponse(f"<h1> details of blog post: {post_id} </h1>")


def user_profile(request,username):
    return HttpResponse(f"<h1> details of blog user: {username} </h1>")

#http://127.0.0.1:8000/blog/post/10/    

def article_by_year(request, year):
    return HttpResponse(f"<h1>Article from the year {year}</h1>")

# def article_details(request,year, month):
#     return HttpResponse(f"<h1> Article from {year} - {month} </h1>")

# def article_details(request, **kwargs):
#     return HttpResponse(f"<h1> data form kwargs year {kwargs['year']} - month {kwargs['month']} </h1>")

#or 

def article_details(request, **kwargs):
    return HttpResponse(f"<h1> data form kwargs {kwargs} </h1>")
    #data form kwargs {'year': 2026, 'month': 8} -> op



