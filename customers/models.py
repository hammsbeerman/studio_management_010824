from django.db import models
from django.urls import reverse

class Customer(models.Model):
    company_name = models.CharField('Company Name', max_length=100, blank=True, null=True)
    first_name = models.CharField('First Name', max_length=100, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=100, blank=True, null=True)
    address1 = models.CharField('Address 1', max_length=100, blank=True, null=True)
    address2 = models.CharField('Adddress 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, blank=True, null=True)
    state = models.CharField('State', max_length=100, blank = True, null=True)
    zipcode = models.CharField('Zipcode', max_length=100, blank=True, null=True)
    phone1 = models.CharField('Phone 1', max_length=100, blank=True, null=True)
    phone2 = models.CharField('Phone 2', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    website = models.URLField('Website', max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(auto_now = True, blank=False, null=False)
    active = models.BooleanField(default=True)



    def get_absolute_url(self):
        return reverse("customers:detail", kwargs={"id": self.id})
    
    def get_hx_url(self):
        #return "/pantry/recipes/"
        return reverse("customers:hx-detail", kwargs={"id": self.id})
    
    def get_edit_url(self):
        return reverse("customers:update", kwargs={"id": self.id})
    
    def get_contacts_children(self):
        return self.customercontact_set.all()

    def __str__(self):
        return self.company_name
    
class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    #company = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    fname = models.CharField('First Name', max_length=100, blank=True, null=True)
    lname = models.CharField('Last Name', max_length=100, blank=True, null=True)
    address1 = models.CharField('Address 1', max_length=100, blank=True, null=True)
    address2 = models.CharField('Adddress 2', max_length=100, blank=True, null=True)
    city = models.CharField('City', max_length=100, blank=True, null=True)
    state = models.CharField('State', max_length=100, blank = True, null=True)
    zipcode = models.CharField('Zipcode', max_length=100, blank=True, null=True)
    phone1 = models.CharField('Phone', max_length=100, blank=True, null=True)
    email = models.EmailField('Email', max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated = models.DateTimeField(auto_now = True, blank=False, null=False)

    def get_absolute_url(self):
        return self.customer.get_absolute_url()
    
    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.customer.id,
            "id": self.id
        }
        return reverse("customers:hx-contact-update", kwargs=kwargs)

    def __str__(self):
        return self.fname


