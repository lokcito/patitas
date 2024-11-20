from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def v_index(request):
    context = {
        "providers": [
            {
                "first_name": "Pepito",
                "last_name": "Rojas",
                "photo": "https://whoofpoint.com/media/images/card_id/profile_73870520.png"
            },
            {
                "first_name": "Juan",
                "last_name": "Ramirez"
            },
            {
                "first_name": "Maria",
                "last_name": "Suarez"
            },
            {
                "first_name": "Vanessa",
                "last_name": "Suarez"
            },
            {
                "first_name": "Michael",
                "last_name": "Suarez"
            },
            {
                "first_name": "Ramiro",
                "last_name": "Suarez"
            },
            {
                "first_name": "Micky",
                "last_name": "Suarez"
            },
        ]
    }

    return render(request, "homepage/index.html", 
                  context)