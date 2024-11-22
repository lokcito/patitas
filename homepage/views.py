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
                "last_name": "Ramirez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile__z9pMJfk.png"
            },
            {
                "first_name": "Maria",
                "last_name": "Suarez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile__Hbemmoz.png"
            },
            {
                "first_name": "Vanessa",
                "last_name": "Suarez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile__Bxs38Zm.png"
            },
            {
                "first_name": "Michael",
                "last_name": "Suarez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile_40442120.png"
            },
            {
                "first_name": "Ramiro",
                "last_name": "Suarez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile_74944414_nzUOEwk.png"
            },
            {
                "first_name": "Micky",
                "last_name": "Suarez",
                "photo": "https://whoofpoint.com/media/images/card_id/profile_75449101.png"
            },
        ]
    }

    return render(request, "homepage/index.html", 
                  context)

def v_feedback_gracias(request):
    return render(request, "homepage/feedback_gracias.html")

from django.shortcuts import redirect
def v_feedback_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("++", data)
        ## Guardar base de datos
        ## Guardar en CSV, Excel
        return redirect("/feedback/gracias")
    
    return redirect("/")