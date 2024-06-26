from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import FormView, CreateView

from main.forms import ZakazForm, Uslugs, RemontForm, ZaprosForm
from main.models import ParticipationApplication, Workers, Uslugs, Zakaz, Remont, User, Zapros


# Create your views here.

def index(request):
    Uslug = Uslugs.objects.all()
    return render(request, 'main/index.html', {"uslugs":Uslug})


def prices(request):
    return render(request, 'main/prices.html')


def reiting(request):
    return render(request, 'main/reiting.html')

# def zapros(request):
#     zapros = zapros.objects.all()
#     return render(request, 'main/zapros.html', )

def Zapros_View(request):
    if request.method == 'POST':
        form = ZaprosForm(request.POST)
        if form.is_valid():
                form.instance.user = request.user
                zapros = form.save(commit=False)
                zapros.save()
                return redirect('/')
    else:
        form = ZaprosForm()
    return render(request, 'main/zapros.html', {'form': form})

def contacts(request):
    return render(request, 'main/contacts.html')


# def forma(request):
    return render(request, 'main/forma.html', context={"user": request.user})

def forma1(request):
    return render(request, 'main/forma1.html', context={"user": request.user})

def profile(request):
    return render(request, 'main/profile.html', context={"profile":request.user.profile})

def zapisi(request):
    remonts = Remont.objects.all().order_by('-data')[:10]
    return render(request, 'main/zapisi.html', {'remonts':remonts})

# class zapisi(CreateView):
#     template_name = "main/zapisi.html"
#     model = Remont
    

#     def get_context_data(self, **kwargs):
#         kwargs["user"] = self.request.user 
#         return super().get_context_data(**kwargs)
    
# def schedule(request):
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
    if request.method == 'POST':
        form = ZakazForm(request.POST)
        if form.is_valid():
                zakaz = form.save(commit=False)
                zakaz.save()
                return redirect('/')
    else:
        form = ZakazForm()
    return render(request, 'main/forma.html', {'form': form})

class ApplicationFormView(CreateView):
    template_name = "main/application_form.html"
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

def sertificate(request):
    return render(request, 'main/sertificate.html')

def workers(request):
    workers = Workers.objects.all()
    return render(request, 'main/workers.html', {'workers':workers})

def create_remont(request):
    if request.method == 'POST':
        form = RemontForm(request.POST)
        if form.is_valid():
            form.instance.mehanik = request.user
            remont = form.save(commit=False)
            remont.save()
            return redirect('/')
    else:
        form = RemontForm()
    return render(request, 'remont.html', {'form': form})