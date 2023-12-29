from django.urls import path

from .views import (
    workorder_list_view,
    create_base,
    contacts,
    workorder_update_view,
    workorder_detail_view,
    workorder_detail_hx_view,
    update_contact,
    workorder_delete_view,
)


app_name='workorders'

urlpatterns = [
    path("", workorder_list_view, name='list'), #List All workorders
    path("createbase/", create_base, name='createbase'), #Create base details of new workorder
    path('contacts/', contacts, name='contacts'), #Fills the contact dropdown on createbase/
    path('updatecontact/', update_contact, name='update-contact'),
    path("hx/<str:id>/", workorder_detail_hx_view, name='hx-detail'),
    path("<str:id>/edit", workorder_update_view, name='update'),
    path("<str:id>/delete", workorder_delete_view, name='delete'),
    path("<str:id>/", workorder_detail_view, name='detail'),
    
]