from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic

from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, "lead_list.html", context=context)


def lead_detail(request, pk):
    lead = Lead.objects.get(pk=pk)
    context = {
        "lead": lead
    }
    return render(request, "lead_detail.html", context=context)


# def lead_create(request):
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                                 first_name=first_name, 
#                                 last_name=last_name, 
#                                 age=age, 
#                                 agent=agent
#                                 )
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "lead_create.html", context)

def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request, "lead_create.html", context)


# def lead_update(request, pk):
#     lead = Lead.objects.get(pk=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()            
#             return redirect("/leads")
#     context = {
#         "form": form
#     }
#     return render(request, "lead_create.html", context)

def lead_update(request, pk):
    lead = Lead.objects.get(pk=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "lead_update.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(pk=pk)
    lead.delete()
    return redirect("/leads")


# CBVs #

class LeadListView(generic.ListView):
    template_name = "lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "lead_create.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadUpdateView(generic.UpdateView):
    template_name = "lead_update.html"
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


class LeadDeleteView(generic.DeleteView):
    template_name = "lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")    