from django.db import models
from django.urls import reverse
from customers.models import Customer, CustomerContact

# Create your models here.
class Workorder(models.Model):
    customer = models.ForeignKey(Customer, blank=False, null=True, on_delete=models.CASCADE)
    contact = models.ForeignKey(CustomerContact, blank=True, null=True, on_delete=models.SET_NULL)
    ##company = models.OneToOneField(Customer, on_delete=models.CASCADE, blank=True, null=True)
    workorder = models.CharField('Workorder', max_length=100, blank=False, null=False, unique=True)
    internal_company = models.CharField('Internal Company', choices=[('LK Design', 'LK Design'), ('Krueger Printing', 'Krueger Printing')], max_length=100, blank=False, null=False)
    description = models.CharField('Description', max_length=100, blank=True, null=True)
    deadline = models.DateField('Deadline', blank=True, null=True)
    budget = models.CharField('Budget', max_length=100, blank=True, null=True)
    quoted_price = models.CharField('Quoted Price', max_length=100, blank=True, null=True)
    original_order = models.CharField('Original Order', max_length=100, blank=True, null=True)


    #def __str__(self):
    #    return self.workorder

    def get_absolute_url(self):
        return reverse("workorders:detail", kwargs={"id": self.workorder})
    
    def get_hx_url(self):
        #return "/pantry/recipes/"
        return reverse("workorders:hx-detail", kwargs={"id": self.id})

    def get_edit_url(self): #reference these, that way changes are only made one place
        return reverse("workorders:update", kwargs={"id": self.id})

    def get_delete_url(self): #reference these, that way changes are only made one place
        return reverse("workorders:delete", kwargs={"id": self.id})

    def get_contacts_children(self):
        return self.contact_set.all()
    
    def get_item_children(self):
        return self.workorderitem_set.all()
    
    def __str__(self):
        return self.workorder
    
class Category(models.Model):
    name = models.CharField('Name', max_length=100, blank=True, null=True)
    description = models.CharField('Description', max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    
class ItemCategory(models.Model):
    workorder = models.ForeignKey(Workorder, blank=False, null=True, on_delete=models.SET_NULL)
    description = models.CharField('Description', max_length=100, blank=False, null=False)
    item_order = models.PositiveSmallIntegerField('Display Order', blank=True, null=True)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    original_item_order = models.CharField('Original Item Order', max_length=100, blank=True, null=True)
    original_item_price = models.CharField('Original Item Price', max_length=100, blank=True, null=True)
    internal_company = models.CharField('Internal Company', choices=[('LK Design', 'LK Design'), ('Krueger Printing', 'Krueger Printing')], max_length=100, blank=False, null=False)

    def __str__(self):
        return self.workorder.workorder + ' -- ' + self.description
    
class WorkorderItem(models.Model):
    workorder = models.ForeignKey(Workorder, blank=False, null=True, on_delete=models.CASCADE)
    item_category = models.ForeignKey(Category, blank=False, null=False, on_delete=models.CASCADE)
    description = models.CharField('Description', max_length=100, blank=False, null=False)
    quantity = models.CharField('Quantity', max_length=100, blank=False, null=False)
    unit_price = models.CharField('Unit Price', max_length=100, blank=False, null=False)
    total_price = models.CharField('Total Price', max_length=100, blank=False, null=False)

    def get_absolute_url(self):
        return self.workorder.get_absolute_url()
    
    def get_hx_edit_url(self):
        kwargs = {
            "parent_id": self.workorder.id,
            "id": self.id
        }
        return reverse("workorders:hx-workorder-item-detail", kwargs=kwargs)




    def __str__(self):
        return self.workorder.workorder + ' -- ' + self.description





    #def get_services_children(self):
    #    return self.workorderservice_set.all()

# class JobDetail(models.Model):
#     class JobQuote(models.TextChoices):
#         WORKORDER = "Workorder"
#         QUOTE = "Quote"

#     class Company(models.TextChoices):
#         LK = "LK"
#         KRUEGER = "KRUEGER"

#     customer = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.SET_DEFAULT, default=2)
#     description = models.CharField('Job Description', max_length=100, blank=False, null=False)
#     jobquote = models.CharField('Workorder or Quote', max_length=100, choices=JobQuote.choices, blank=False, null=False)
#     company = models.CharField('Company', max_length=100, choices=Company.choices, blank=False, null=False)



