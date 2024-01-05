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
    workorder_item_update_hx_view, #Was workorder_invoice_update_hx_view
    add_item,
    item_list,
    edit_item,
    workorder_item_list_view,
    remove_workorder_item,
    #edit_right,
    modal,

)


app_name='workorders'

urlpatterns = [
    path("", workorder_list_view, name='list'), #List All workorders
    path("createbase/", create_base, name='createbase'), #Create base details of new workorder
    path('contacts/', contacts, name='contacts'), #Fills the contact dropdown on createbase/
    path('updatecontact/', update_contact, name='update-contact'),
    path('modal/', modal, name='modal'),
    #
    #
    path('add/<int:parent_id>/', add_item, name='add_item'),
    path('items/', item_list, name='item_list'),
    #path('items/<int:pk>/edit/<int:cat>/', edit_item, name='edit_item'),
    path('items/<int:pk>/edit/<int:cat>', edit_item, name='edit_item'),
    #path('items/<int:pk>/editright/', edit_right, name='edit_right'),
    path('items/<int:pk>/remove/', remove_workorder_item, name='remove_item'),
    #
    path("item/<int:id>/", workorder_item_list_view, name='workorder_item_list'),
    #
    path("hx/<str:parent_id>/invoice/", workorder_item_update_hx_view, name='hx-item-add'),
    path("hx/<str:parent_id>/item/", workorder_item_update_hx_view, name='hx-item-create'),
    path("hx/<str:parent_id>/item/<int:id>/", workorder_item_update_hx_view, name='hx-workorder-item-detail'),
    path("hx/<str:id>/", workorder_detail_hx_view, name='hx-detail'),
    path("<str:id>/edit", workorder_update_view, name='update'),
    path("<str:id>/delete", workorder_delete_view, name='delete'),
    path("<str:id>/", workorder_detail_view, name='detail'),
    
]