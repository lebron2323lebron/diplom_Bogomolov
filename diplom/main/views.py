from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, CreateView

from main.forms import ApplicationForm, ZakazForm, Uslugs
from main.models import ParticipationApplication, Course, Workers, Uslugs, Zakaz


# Create your views here.

def index(request):
    Uslug = Uslugs.objects.all()
    return render(request, 'main/index.html', {"uslugs":Uslug})


def prices(request):
    return render(request, 'main/prices.html')


def cources(request):
    return render(request, 'main/cources.html')

def course1(request):
    return render(request, 'main/course1.html')

def course2(request):
    return render(request, 'main/course2.html')

def course3(request):
    return render(request, 'main/course3.html')

def reiting(request):
    return render(request, 'main/reiting.html')


def contacts(request):
    return render(request, 'main/contacts.html')


# def forma(request):
    return render(request, 'main/forma.html', context={"user": request.user})

def forma1(request):
    return render(request, 'main/forma1.html', context={"user": request.user})

def profile(request):
    return render(request, 'main/profile.html', context={"profile":request.user.profile})


def profile_courses(request):
    return render(request, "main/profile-courses.html", context={"courses": request.user.courses.all()})



class zapisi(CreateView):
    template_name = "main/zapisi.html"
    model = ParticipationApplication
    form_class = ApplicationForm

    def get_context_data(self, **kwargs):
        kwargs["user"] = self.request.user 
        return super().get_context_data(**kwargs)
    
def schedule(request):
    profiles = ParticipationApplication.objects.all()
    return render(request, 'main/zapisi.html', {'profiles': profiles})

# class Zakaz(CreateView):
    template_name = "main/forma.html"
    form_class = Zakaz
    model = Zakaz

    def get_context_data(self, **kwargs):
        kwargs["user"] = self.request.user
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = self.request.user
        Uslugs = form.cleaned_data["uslugs"]
        form.instance.Uslugs = Uslugs
        form.instance.user = user
        user.zakaz.add(Zakaz)
        # print(dir(form))
        # print(form.cleaned_data)
        return super().form_valid(form)

def Zakaz_view(request):
    form = ZakazForm()
    return render(request, 'main/forma.html', {'form': form})

class ApplicationFormView(CreateView):
    template_name = "main/application_form.html"
    form_class = ApplicationForm
    success_url = "/profile-courses"
    model = ParticipationApplication

    def get_context_data(self, **kwargs):
        kwargs["user"] = self.request.user
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = self.request.user
        course = form.cleaned_data["course"]
        form.instance.course = course
        form.instance.user = user
        user.courses.add(course)
        # print(dir(form))
        # print(form.cleaned_data)
        return super().form_valid(form)

def about(request):
    return render(request, "main/about_us.html")

def course1(request):
    return render(request, 'main/course1.html')

def course2(request):
    return render(request, 'main/course2.html')

def course3(request):
    return render(request, 'main/course3.html')

def module(request):
    cources = Course.objects.all()
    return render(request, "main/modules.html", {'cources' : cources})

def sertificate(request):
    return render(request, 'main/sertificate.html')

def workers(request):
    workers = Workers.objects.all()
    return render(request, 'main/workers.html', {'workers':workers})