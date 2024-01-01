from django.db import models

class Service(models.Model):
    name = models.CharField('Name', max_length=100, blank=False, null=False, unique=True)
    #category = models.ForeignKey(ProductCategory, blank=True, null=True, on_delete=models.SET_NULL)
    master_part_number = models.CharField('Master Part Number', max_length=100, blank=True, null=True)
    description = models.CharField('Description', max_length=100, blank=True, null=True)
    price = models.CharField('Price', max_length=100, blank=True, null=True)
    #measurement = models.ForeignKey(Measurement, blank=True, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now = True, blank=False, null=False)
    active= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    #class Meta:
    #    ordering = ["category", "name"]

    #class Meta:
    #    ordering = ["category", "-name"]
