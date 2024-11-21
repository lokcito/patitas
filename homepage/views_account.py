from django.shortcuts import redirect, render

def v_sign_up(request):
    return render(request, "homepage/account/sign_up.html")

def v_sign_up_create(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("=>>>>", data)
        # Enviamos el email
        return redirect("/sign_up/thank_you")
    return redirect("/")

def v_sign_up_thank_you(request):
    return render(request, "homepage/account/thank_you.html")