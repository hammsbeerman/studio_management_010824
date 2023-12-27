from django.urls import path

from .views import (
    customer_create_view,
    customer_list_view,
    customer_detail_view,
    customer_detail_hx_view,
    customer_update_view,
    customer_contact_update_hx_view,
)

app_name='customers'

urlpatterns = [
    path("", customer_list_view, name='list'),
    path("create/", customer_create_view, name='create'),
    path("hx/<int:parent_id>/contact/<int:id>/", customer_contact_update_hx_view, name='hx-contact-update'),
    path("hx/<int:parent_id>/contact/", customer_contact_update_hx_view, name='hx-contact-create'),
    #path("name-autosuggest/", autosuggest, name='name-autosuggest'),
    path("hx/<int:id>/", customer_detail_hx_view, name='hx-detail'),
    path("<int:id>/edit/", customer_update_view, name='update'),
    path("<int:id>/", customer_detail_view, name='detail'),
]