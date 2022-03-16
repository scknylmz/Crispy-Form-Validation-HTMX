from re import X
from tempfile import tempdir
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form
from django.contrib.auth import login

from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field

from .forms import UniversityForm
# Create your views here.

def index(request):
    if request.method == "GET":
        form = UniversityForm()
        context={
            "form" : form,
        }
        return render(request, "index.html", context)
    
    elif request.method == "POST":
        form = UniversityForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            template = render(request, 'profile.html')
            template['Hx-Push'] = '/profile/'
            return template

        else:
            ctx = {}
            ctx.update(csrf(request))
            form_html = render_crispy_form(form, context=ctx)
            return HttpResponse(form_html)
            

#def check_username(request):
    #form = UniversityForm(request.GET)
    # print(as_crispy_field(form['username']))    # request.GET => {'username' : ['username inputuna ne yazdıysan onu getiriyor]}
                                                # as_crispy_field(form['username]) => 

    #return HttpResponse(as_crispy_field(form['username']))

def check_username(request):
    form = UniversityForm(request.GET)
    if form.is_valid():
        valid = True
    else:
        valid = False    
    
    context = {
        'field' : as_crispy_field(form['username']),
        'valid' : valid
    }
    
    return render(request, 'partials/field.html', context)

#def check_subject(request):
#    form = UniversityForm(request.GET)
#   return HttpResponse(as_crispy_field(form['subject']))

def check_subject(request):
    form = UniversityForm(request.GET)
    if form.is_valid():
        valid = True
    else:
        valid = False    
    
    context = {
        'field' : as_crispy_field(form['subject']),
        'valid' : valid
    }
    return render(request, 'partials/field.html', context)