from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {"is_root": request.path == "/"}
    return render(request, "home.html", context)

def about(request):
    context = {"is_about_page": request.path == "/about/"}
    return render(request, "about.html", context)

def projects(request):
    context = {"is_projects_page": request.path == "/projects/"}
    return render(request, "projects.html", context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        return HttpResponse(f"Thank you, {name}! Your message has been received.")
    context = {"is_contact_page": request.path == "/contact/"}
    return render(request, 'contact.html', )