from django.forms.models import modelformset_factory
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .forms import CustomerForm, CustomerContactForm
from .models import Customer, CustomerContact

# def customer_create_view(request):
#     form = CustomerForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = request.user
#         obj.save()
#         return redirect(obj.get_absolute_url())
#         #return redirect(obj.get_hx_url())
#     return render(request, "customers/add-update.html", context)

def customer_detail_view(request, id=None):
    #obj = get_object_or_404(Recipe, id=id, user=request.user)
    hx_url = reverse("customers:hx-detail", kwargs={"id": id})
    context = {
        "hx_url": hx_url,
    }
    return render(request, "customers/detail.html", context)

def customer_detail_hx_view(request, id=None):
    if not request.htmx:
        raise Http404
    try:
        #obj = Customer.objects.get(id=id, user=request.user)
        obj = Customer.objects.get(id=id)
    except:
        obj = None
    if obj is None:
        #raise Http404
        return HttpResponse("Not Found.")
    context = {
        "object": obj
    }
    return render(request, "customers/partials/detail.html", context)


def customer_create_view(request):
    form = CustomerForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        cn = request.POST.get('company_name')
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        if not cn and not fn and not ln:
            message = 'Please fill in Company name or Customer Name'
            context = {
                "message": message,
                "form": form
            }
            #return render(request, "customers/add-update.html", context)
            return render(request, "customers/partials/forms.html", context)
        if not cn:
            #print('Empty string')
            obj.company_name = fn + ' ' + ln    
        #else:
            #print(cn) 
        #print(request.POST)
        obj.user = request.user
        obj.save()
        if request.htmx:
            headers = {
                "HX-Redirect": obj.get_absolute_url()
            }
            return HttpResponse("Created", headers=headers)
        return redirect(obj.get_absolute_url())
    return render(request, "customers/add-update.html", context)

def customer_list_view(request):
    #qs = Customer.objects.filter(user=request.user)
    qs = Customer.objects.all()
    context = {
        "object_list": qs
    }
    return render(request, "customers/list.html", context)

def customer_update_view(request, id=None):
    #obj = get_object_or_404(Customer, id=id, user=request.user)
    obj = get_object_or_404(Customer, id=id)
    form = CustomerForm(request.POST or None, instance=obj)
    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    new_contact_url = reverse("customers:hx-contact-create", kwargs={"parent_id": obj.id})
    context = {
        "form": form,
        "new_contact_url": new_contact_url,
        "object": obj
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'
    if request.htmx:
        return render(request, "customers/partials/forms.html", context)
    return render(request, "customers/add-update.html", context)  

def customer_contact_update_hx_view(request, parent_id=None, id=None):
    if not request.htmx:
        raise Http404
    try:
        #parent_obj = Customer.objects.get(id=parent_id, user=request.user)
        parent_obj = Customer.objects.get(id=parent_id)
    except:
        parent_obj = None
    if parent_obj is None:
        return HttpResponse("Not found.")
    
    instance = None
    if id is not None:
        try:
            instance = CustomerContact.objects.get(customer=parent_obj, id=id)
        except:
            instance = None   
    form = CustomerContactForm(request.POST or None, instance=instance)
    #url = instance.get_hx_edit_url() if instance else reverse("recipes:hx-ingredient-create", kwargs={"parent_id": parent_obj.id})
    url = reverse("customers:hx-contact-create", kwargs={"parent_id": parent_obj.id})
    if instance:
        #print (request.POST.get('fname'))
        url = instance.get_hx_edit_url()
    context = {
        "url": url,
        "form": form,
        "object": instance
    }
    if form.is_valid():
        new_obj = form.save(commit=False)
        if instance is None:
            new_obj.customer = parent_obj
        new_obj.save()
        context['object'] = new_obj
        return render(request, "customers/partials/contact-inline.html", context)
    return render(request, "customers/partials/contact-form.html", context)

