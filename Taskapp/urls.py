from django.contrib import admin
from django.urls import path,include
from Taskapp import views

urlpatterns = [
    path('', views.sales_list, name='sales_list'),
    path('sales/add/', views.sales_add, name='sales_add'),
    path('sales/edit/<int:pk>/', views.sales_edit, name='sales_edit'),
    # path('sales/download/', views.Download_sales_csv, name='sales_download'),
    path("import/", views.import_sales_csv, name="import_sales_data"),
    path('get-countries/', views.get_countries, name='get_countries'),
    path('delete/<int:pk>/', views.get_deleted_records, name='delete_record'),

]