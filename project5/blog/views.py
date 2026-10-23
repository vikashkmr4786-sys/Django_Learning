from django.shortcuts import render
from datetime import datetime

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def home(request):
    context = {"name": "vikash Kumar",
    "age": 22,
    "skills":["python", "django", "react"],
    "user": User("kumar pandit",33),
    "blog":{
        "title": "Django templates intro",
        "content": "<b>This is Bold </b>",
        "created_at": datetime(2026,8,18,10,30) 
        # //Created date : Aug. 18, 2026, 10:30 a.m.
    },
    "empty_value": "None",
    }
    return render(request,"blog/home.html",context)