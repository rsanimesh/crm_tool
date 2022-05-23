from django.urls import path
from core.views.table_views import *
from core.views.auth_views import token_login,token_logout
from core.views.table_agg_views import *


urlpatterns = [
    path('create-company/', CompanyCreate.as_view(), name='create-company'),
    path('list-company/', CompanyList.as_view(), name='list-company'),
    path('list-company/<int:pk>/', CompanyDetail.as_view(), name='retrieve-company'),
    path('update-company/<int:pk>/', CompanyUpdate.as_view(), name='update-company'),
    path('delete-company/<int:pk>/', CompanyDelete.as_view(), name='delete-company'),

    path('create-table/', TableCreate.as_view(), name='create-table'),
    path('list-table/', TableList.as_view(), name='list-table'),
    path('list-table/<int:pk>/', TableDetail.as_view(), name='retrieve-table'),
    path('update-table/<int:pk>/', TableUpdate.as_view(), name='update-table'),
    path('delete-table/<int:pk>/', TableDelete.as_view(), name='delete-table'),

    path('create-fields/', FieldsCreate.as_view(), name='create-fields'),
    path('list-fields/', FieldsList.as_view(), name='list-fields'),
    path('list-fields/<int:pk>/', FieldsDetail.as_view(), name='retrieve-fields'),
    path('update-fields/<int:pk>/', FieldsUpdate.as_view(), name='update-fields'),
    path('delete-fields/<int:pk>/', FieldsDelete.as_view(), name='delete-fields'),

    path('token-login', token_login, name='token_login'),
    path('token-logout', token_logout, name='token_logout'),
    
    path('table-data-list', table_data_list, name="table-data-list"),
    path('add-row', add_row, name="add-row"),
    path('delete-row', delete_row, name='delete_row'),
    path('update-row', update_row, name='update_row'),
] 
