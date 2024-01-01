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
    add_movie,
    movie_list,
    edit_movie,
    workorder_item_list_view,

)


app_name='workorders'

urlpatterns = [
    path("", workorder_list_view, name='list'), #List All workorders
    path("createbase/", create_base, name='createbase'), #Create base details of new workorder
    path('contacts/', contacts, name='contacts'), #Fills the contact dropdown on createbase/
    path('updatecontact/', update_contact, name='update-contact'),
    #
    #
    path('add/', add_movie, name='add_movie'),
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>/edit/', edit_movie, name='edit_movie'),
    #
    path("item/<str:id>", workorder_item_list_view, name='workorder_item_list'),
    #
    path("hx/<str:parent_id>/invoice/", workorder_item_update_hx_view, name='hx-item-add'),
    path("hx/<str:parent_id>/item/", workorder_item_update_hx_view, name='hx-item-create'),
    path("hx/<str:parent_id>/item/<int:id>/", workorder_item_update_hx_view, name='hx-workorder-item-detail'),
    path("hx/<str:id>/", workorder_detail_hx_view, name='hx-detail'),
    path("<str:id>/edit", workorder_update_view, name='update'),
    path("<str:id>/delete", workorder_delete_view, name='delete'),
    path("<str:id>/", workorder_detail_view, name='detail'),
    
]