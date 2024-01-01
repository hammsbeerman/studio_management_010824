from multiprocessing import parent_process
from urllib.request import Request
#from winreg import REG_WHOLE_HIVE_VOLATILE

from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory #modelform for querysets
from django.urls import reverse
from django.http import Http404
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django import forms
from django.forms import modelform_factory

from .models import Workorder, WorkorderItem
from customers.models import Customer, CustomerContact
#from inventory.models import Service, Inventory
from .forms import WorkorderForm, WorkorderItemForm

def add_movie(request):
    if request.method == "POST":
        form = WorkorderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'movieListChanged'})
    else:
        form = WorkorderItemForm()
    return render(request, 'workorders/partials/movie_form.html', {
        'form': form,
    })

def movie_list(request):
    return render(request, 'workorders/partials/movie_list.html', {
        'items': WorkorderItem.objects.all(),
    })

def edit_movie(request, pk):
    item = get_object_or_404(WorkorderItem, pk=pk)
    if request.method == "POST":
        form = WorkorderItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'movieListChanged'})
    else:
        form = WorkorderItemForm(instance=item)
    return render(request, 'workorders/partials/movie_form.html', {
        'form': form,
        'item': item,
    })


def workorder_list_view(request):
    #qs = Customer.objects.filter(user=request.user)
    qs = Workorder.objects.all().order_by('-workorder')
    context = {
        "object_list": qs
    }
    return render(request, "workorders/list.html", context)

def create_base(request):
    context = {}
    if request.method == "GET":
        customers = Customer.objects.all()
        context = {'customers': customers}
        return render(request, 'workorders/create-workorder.html', context)
    print(request.POST)
    if request.method == "POST":
        customer = request.POST.get("customer")
        contact = request.POST.get("contact")
        workorder = request.POST.get("workorder")
        description = request.POST.get("description")
        deadline = request.POST.get("deadline")
        budget = request.POST.get("budget")
        quoted_price = request.POST.get("quoted_price")
        workorder = (workorder.upper())
        if customer == "0":
            customers = Customer.objects.all()
            context = {'customers': customers}
            context['error'] = 'Please select a customer'
            return render(request, 'workorders/create-workorder.html', context)
        if not workorder:
            customers = Customer.objects.all()
            context = {'customers': customers}
            context['workordererror'] = 'Please enter a workorder'
            return render(request, 'workorders/create-workorder.html', context)
        #if contact == 0: -- Contacts are optional at this point
        #    context['error']
        #    return render(request, 'workorders/create-workorder.html', context)   
        try:
            obj = Workorder.objects.create(customer_id=customer, contact_id=contact, workorder=workorder, description=description, deadline=deadline, budget=budget, quoted_price=quoted_price)
        except:
            customers = Customer.objects.all()
            context = {'customers': customers}
            context['workordererror'] = 'That workorder already exists'
            return render(request, 'workorders/create-workorder.html', context)
        context['workorder'] = workorder #return workorder number to form
        context['created'] = True
        return redirect(obj.get_edit_url())
    return render(request, "workorders/create-workorder.html", context=context)

def contacts(request):
    customer = request.GET.get('customer')
    contacts = CustomerContact.objects.filter(customer=customer)
    context = {'contacts': contacts}
    return render(request, 'workorders/partials/contact-dropdown.html', context)

def workorder_update_view(request, id=None):
    obj = get_object_or_404(Workorder, id=id,)
    form = WorkorderForm(request.POST or None, instance=obj) #instance=obj fills the form with data
    titles = ('true')
    new_item_url = reverse("workorders:hx-item-add", kwargs={"parent_id": obj.id})
    #new_invoice_url = reverse("workorders:hx-invoice-add", kwargs={"parent_id": obj.id})
    # new_service_url = reverse("workorders:hx-service-create", kwargs={"parent_id": obj.id})
    # new_inventory_url = reverse("workorders:hx-inventory-create", kwargs={"parent_id": obj.id})
    # new_noninventory_url = reverse("workorders:hx-noninventory-create", kwargs={"parent_id": obj.id})
    #WorkorderServiceFormset = modelformset_factory(WorkorderService, form=WorkorderServiceForm, extra=1)
    #qs = obj.contact_set.all()
    context = {
        "form": form,
        #"formset": formset,
        "object": obj,
        "titles": titles,
        "new_item_url": new_item_url,
        # "new_invoice_url": new_invoice_url,
        # "new_service_url": new_service_url,
        # "new_inventory_url": new_inventory_url,
        # "new_noninventory_url": new_noninventory_url
    }
    #print(form)
    if all([form.is_valid()]):
    #if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        context['message'] = ''
    if request.htmx:
        return render(request, "workorders/partials/forms.html", context)
    return render(request, "workorders/add-update.html", context)

def workorder_detail_view(request, id=None):
    hx_url = reverse("workorders:hx-detail", kwargs={"id": id})
    context = {
        "hx_url": hx_url
    }
    return render(request, "workorders/detail.html", context)

def workorder_detail_hx_view(request, id=None):
    if not request.htmx:
        print("Here 1")
        raise Http404
    try:
        obj = Workorder.objects.get(workorder=id)
        print("Here 2")
        print(obj)
    except:
        obj = None
        print("Here 3")
    if obj is  None:
        print("Here 4")
        return HttpResponse("Not found.")
    context = {
        "object": obj
    }
    #print (object.line_total_default)
    print("Here 5")
    return render(request, "workorders/partials/detail.html", context) 

def update_contact(request):
    customer = request.GET.get('customer')
    currentcontact = request.GET.get('contact')
    contacts = CustomerContact.objects.filter(customer=customer)
    if currentcontact != 'None':
        currentcontact = CustomerContact.objects.filter(id=currentcontact)
    if currentcontact == 'None':
        currentcontact = '0'
    context = {
        'contacts': contacts,
        'currentcontact': currentcontact
    }
    #print(contacts)
    #print(currentcontact)
    return render(request, 'workorders/partials/contact-update.html', context)

def workorder_delete_view(request, id=None):
    #hx_url = reverse("workorders:hx-detail", kwargs={"id": id})
    obj = get_object_or_404(Workorder, id=id,)
    if request.method == "POST":
        obj.delete()
        success_url = reverse('workorders:list')
        return redirect(success_url)
        #return render 
    context = {
        #"hx_url": hx_url
        "object": obj
    }
    return render(request, "workorders/delete.html", context)


def workorder_item_update_hx_view(request, parent_id= None, id=None):
    if not request.htmx:
        raise Http404
    try:
        parent_obj = Workorder.objects.get(id=parent_id)
    except:
        parent_obj = None
    if parent_obj is  None:
        return HttpResponse("Not found.")
    instance = None
    #print (id)
    if id is not None:
        try:
            instance = WorkorderItem.objects.get(workorder=parent_obj, id=id)
        except:
            instance = None
    form = WorkorderItemForm(request.POST or None, instance=instance)
    url = reverse("workorders:hx-item-create", kwargs={"parent_id": parent_obj.id})  ###
    #services = Service.objects.all().order_by('-name')
    if instance:
        url = instance.get_hx_edit_url()
        print(instance)
        print(url)
    context = {
        "url": url,
        "form": form,
        "object": instance,
    #    "services": services
    }
    if form.is_valid():
        new_obj=form.save(commit=False)
        if instance is None:
            new_obj.workorder = parent_obj
        # cr = request.POST.get("custom_rate")
        # print(cr)
        # print(new_obj.custom_rate)
        # if cr != '':
        #     cr = float(cr)
        #     print('$' + format(cr, ',.2f'))
        #     new_obj.custom_rate = cr
        new_obj.save()
        context['object'] = new_obj
        print('1')
        return render(request, "workorders/partials/item-inline.html", context)
    if id == None:
        #print(context)
        print('2')
        return render(request, "workorders/partials/item-add-form.html", context)
    if request.htmx:
        print('3')
        return render(request, "workorders/partials/item-form.html", context)
    print('4')
    return render(request, "workorders/partials/item-form.html", context)


class ItemForm(forms.ModelForm):
    class Meta:
        model = WorkorderItem
        exclude = []

def item_table(request):
    #qs = Customer.objects.filter(user=request.user)
    #qs = Workorder.objects.all().order_by('-workorder')
    context = {
    }
    return render(request, "workorders/table.html", context)

def get_item_list(request):
    context ={}
    context['items'] = WorkorderItem.objects.all()
    return render(request, 'workorders/partials/item_list.html', context)

def add_item(request):
    context = {'form': ItemForm()}
    return render(request, 'workorders/partials/add_item.html', context)

def submit_new_item(request):
    context = {}
    form = ItemForm(request.POST)
    context['form'] = form
    if form.is_valid():
        context['item'] = form.save()
    else:
        return render(request, 'workorders/partials/add_item.html', context)
    return render(request, 'workorders/partials/item_row.html', context)

def cancel_add_item(request):
    return HttpResponse()

def delete_item(request, item):
    item = WorkorderItem.objects.get(pk=item)
    item.delete()
    return HttpResponse()

def edit_item(request, item_pk=None):
    item = WorkorderItem.objects.get(pk=item_pk)
    context = {}
    context['item'] = item
    context['form'] = ItemForm(initial={
        'workorder':item.workorder,
        'item_category': item.item_category,
        'description': item.description,
        'age': item.age,
        'major': item.major
    })
    return render(request, 'workorders/partials/edit_item.html', context)

def edit_item_submit(request, item_pk=None):
    context = {}
    item = WorkorderItem.objects.get(pk=item_pk)
    context['item'] = item
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'workorders/partials/edit_item.html', context)
    return render(request, 'workorders/partials/item_row.html', context)