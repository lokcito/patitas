from django.shortcuts import redirect, render

def v_sign_up(request):
    return render(request, "homepage/account/sign_up.html")

def v_sign_up_create(request):
    if request.method == "POST":
        # Captura data
        data = request.POST.copy()
        print("=>>>>", data)

        # Importacion de librerias
        import os
        import resend

        # Definicion de token para el servicio
        resend.api_key = "re_Kn78HRwU_F7uK8HejaweGxsExXpUxqpnE"

        # Definir quien envia el correo y a donde va el correo
        params: resend.Emails.SendParams = {
            "from": "Bichito <robot@resend.equisd.com>",
            "to": [ data["email"] ],
            "subject": "Patitas te da la bienvenida!",
            "html": "<h2>Ya eres parte de Patitas!</h2>"
        }
        email_id = resend.Emails.send(params) # Envia el correo

        # Enviamos el email
        return redirect("/sign_up/thank_you")
    return redirect("/")

def v_sign_up_thank_you(request):
    return render(request, "homepage/account/thank_you.html")


def v_sign_in(request):
    return render(request, "homepage/account/sign_in.html")
def v_sign_in_members(request):
    return render(request, "homepage/account/sign_in_members.html")

def v_sign_in_login(request):
    if request.method == "POST":
        data = request.POST.copy()
        print("+++++++", data)
        return redirect("/sign_in/members")
    return redirect("/")