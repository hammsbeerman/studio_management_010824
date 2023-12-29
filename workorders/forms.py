from django.utils.safestring import mark_safe
from django import forms
from .models import Workorder
from customers.models import Customer, CustomerContact
from dynamic_forms import DynamicField, DynamicFormMixin

class WorkorderForm(DynamicFormMixin, forms.ModelForm):
    required_css_class = 'required-field'
    description = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Workorder
        fields = ['contact', 'workorder', 'description', 'deadline', 'budget', 'quoted_price']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            #print(field)
            new_data = {
                "placeholder": f'{str(field)}',
                "class": 'form-control',
                #"hx-post": "",
                #"hx-trigger": "keyup changed delay:500ms",
                #"hx-target": "#recipe-container",
                #"hx-swap": "outerHTML"
            }
            self.fields[str(field)].widget.attrs.update(
                new_data
            )
        self.fields['description'].widget.attrs.update({'rows': '2'})
        self.fields['contact'].label = ''