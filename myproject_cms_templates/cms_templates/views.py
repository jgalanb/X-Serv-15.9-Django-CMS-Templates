from django.shortcuts import render
from django.http import HttpResponse
from models import Pages
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def administracion(request):
    autentificacion = request.user.is_authenticated()
    if autentificacion == True:
        http_Auth = "<h3>Bienvenido a My Project Cms Templates " + \
                    request.user.username + \
                    "</h3><p>Usuario autentificado: " + \
                    request.user.username + \
                    "<p>Puedes cerrar sesion en el siguiente enlace: " +\
                    "<a href='/logout'>Logout</a></p>"
    else:
        http_Auth = "<h3>Bienvenido a My Project Cms Templates" + \
                    "</h3><p>Puedes iniciar sesion en el siguiente enlace: " +\
                    "<a href='/login'>Login</a></p>"

    return http_Auth

def usuario(request):
    http_Auth = administracion(request)

    return HttpResponse(http_Auth)

@csrf_exempt
def id_to_page(request, identificador):
    http_Auth = administracion(request)
    metodo = request.method
    if metodo == "GET":
        try:
            elementos = Pages.objects.get(id=identificador)
            http_Resp = elementos.page
        except Pages.DoesNotExist:
            http_Error = "<h3><font color='red'>Error! No existe dicho identificador " +\
                        " en el modelo Pages!</font></h3>"
    elif metodo == "PUT":
        http_Error = "<h3><font color='red'>Error! Cuando se introduce un " +\
                    "identificador, el unico metodo valido es GET.</font></h3>"
    else:
        http_Error = "<h3><font color='red'>Error! Metodo no valido. Solo " +\
                    "GET o PUT</font></h3>"
    try:
        return HttpResponse(http_Auth + http_Resp)
    except UnboundLocalError:
        return HttpResponse(http_Error)

@csrf_exempt
def id_to_page_annotated(request, identificador):
    http_Auth = administracion(request)
    metodo = request.method
    if metodo == "GET":
        try:
            elementos = Pages.objects.get(id=identificador)
            http_Resp = elementos.page
        except Pages.DoesNotExist:
            http_Error = "<h3><font color='red'>Error! No existe dicho identificador " +\
                        " en el modelo Pages!</font></h3>"
    elif metodo == "PUT":
        http_Error = "<h3><font color='red'>Error! Cuando se introduce un " +\
                    "identificador, el unico metodo valido es GET.</font></h3>"
    else:
        http_Error = "<h3><font color='red'>Error! Metodo no valido. Solo " +\
                    "GET o PUT</font></h3>"
    try:
        template = get_template('plantilla.html')
        return HttpResponse(template.render(Context({'login': http_Auth,
                'contenido': http_Resp})))
    except UnboundLocalError:
        return HttpResponse(http_Error)

@csrf_exempt
def name_to_page(request, recurso):
    http_Auth = administracion(request)
    metodo = request.method
    if metodo == "GET":
        try:
            elementos = Pages.objects.get(name=recurso)
            http_Resp = elementos.page
        except Pages.DoesNotExist:
            http_Error = "<h3><font color='red'>Error! No existe dicho recurso " +\
                        " en el modelo Pages!</font></h3>"
    elif metodo == "PUT":
        autentificacion = request.user.is_authenticated()
        if autentificacion == True:
            try:
                elementos = Pages.objects.get(name=recurso)
                http_Error = "Cuidado! Este recurso ya esta en la base de datos!"
            except Pages.DoesNotExist:
                cuerpo = request.body
                new_page = Pages(name=recurso, page=cuerpo)
                new_page.save()
                http_Resp = "<p>Se ha introducido el recurso " + recurso +\
                            " en la base de datos.</p>" +\
                            "<p>Accede a la lista de a traves de /pages</p>"
        else:
            http_Error = "Error! No puedes cambiar el contenido de la pagina. " + \
                        "Solo usuarios que esten autentificados"
    else:
        http_Error = "<h3><font color='red'>Error! Metodo no valido. Solo " +\
                        "GET o PUT</font></h3>"

    try:
        return HttpResponse(http_Auth + http_Resp)
    except UnboundLocalError:
        return HttpResponse(http_Error)

@csrf_exempt
def name_to_page_annotated(request, recurso):
    http_Auth = administracion(request)
    metodo = request.method
    if metodo == "GET":
        try:
            elementos = Pages.objects.get(name=recurso)
            http_Resp = elementos.page
        except Pages.DoesNotExist:
            http_Error = "<h3><font color='red'>Error! No existe dicho recurso " +\
                        " en el modelo Pages!</font></h3>"
    elif metodo == "PUT":
        autentificacion = request.user.is_authenticated()
        if autentificacion == True:
            try:
                elementos = Pages.objects.get(name=recurso)
                http_Error = "Cuidado! Este recurso ya esta en la base de datos!"
            except Pages.DoesNotExist:
                cuerpo = request.body
                new_page = Pages(name=recurso, page=cuerpo)
                new_page.save()
                http_Resp = "<p>Se ha introducido el recurso " + recurso +\
                            " en la base de datos.</p>" +\
                            "<p>Accede a la lista de a traves de /pages</p>"
        else:
            http_Error = "Error! No puedes cambiar el contenido de la pagina. " + \
                        "Solo usuarios que esten autentificados"
    else:
        http_Error = "<h3><font color='red'>Error! Metodo no valido. Solo " +\
                        "GET o PUT</font></h3>"

    try:
        template = get_template('plantilla.html')
        return HttpResponse(template.render(Context({'login': http_Auth,
                'contenido': http_Resp})))
    except UnboundLocalError:
        return HttpResponse(http_Error)

def obtener_lista(request):
    http_Auth = administracion(request)
    http_inicial = "<h3>Lista de Pages actualmente en la base de datos:</h3>"
    try:
        elementos = Pages.objects.all()
        if len(elementos) == 0:
            http_Resp = "<h5><font color='red'>La lista Pages esta actualmente " +\
                        "vacia</font></h5>"
            return HttpResponse(http_Resp)
        else:
            http_Resp = '<ol>'
            for elemento in elementos:
                http_Resp += '<li><a href="/' + str(elemento.id) + '">' + \
                            str(elemento.name) + '</a>'
            http_Resp += '</ol>'

    except Pages.DoesNotExist:
        http_Error = "<h3><font color='red'>Error! No existe el modelo " +\
                    "Pages!</font></h3>"

    try:
        return HttpResponse(http_Auth + http_inicial + http_Resp)
    except UnboundLocalError:
        return HttpResponse(http_Error)

def obtener_lista_annotated(request):
    http_Auth = administracion(request)
    http_inicial = "<h3>Lista de Pages actualmente en la base de datos:</h3>"
    try:
        elementos = Pages.objects.all()
        if len(elementos) == 0:
            http_Resp = "<h5><font color='red'>La lista Pages esta actualmente " +\
                        "vacia</font></h5>"
            return HttpResponse(http_Resp)
        else:
            http_Resp = '<ol>'
            for elemento in elementos:
                http_Resp += '<li><a href="/' + str(elemento.id) + '">' + \
                            str(elemento.name) + '</a>'
            http_Resp += '</ol>'

    except Pages.DoesNotExist:
        http_Error = "<h3><font color='red'>Error! No existe el modelo " +\
                    "Pages!</font></h3>"

    try:
        template = get_template('plantilla.html')
        return HttpResponse(template.render(Context({'login': http_Auth,
                'contenido': http_inicial + http_Resp})))
    except UnboundLocalError:
        return HttpResponse(http_Error)
