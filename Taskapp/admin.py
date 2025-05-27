from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import DateWidget
from .models import SalesRecord

class SalesRecordResource(resources.ModelResource):
    order_id = fields.Field(attribute='order_id', column_name='Order ID')
    region = fields.Field(attribute='region', column_name='Region')
    country = fields.Field(attribute='country', column_name='Country')
    item_type = fields.Field(attribute='item_type', column_name='Item Type')
    sales_channel = fields.Field(attribute='sales_channel', column_name='Sales Channel')
    order_priority = fields.Field(attribute='order_priority', column_name='Order Priority')


    order_date = fields.Field(
        attribute='order_date',
        column_name='Order Date',
        widget=DateWidget(format='%d/%m/%Y')
    )
    ship_date = fields.Field(
        attribute='ship_date',
        column_name='Ship Date',
        widget=DateWidget(format='%d/%m/%Y')
    )

    units_sold = fields.Field(attribute='units_sold', column_name='Units Sold')
    unit_price = fields.Field(attribute='unit_price', column_name='Unit Price')
    unit_cost = fields.Field(attribute='unit_cost', column_name='Unit Cost')
    total_revenue = fields.Field(attribute='total_revenue', column_name='Total Revenue')
    total_cost = fields.Field(attribute='total_cost', column_name='Total Cost')
    total_profit = fields.Field(attribute='total_profit', column_name='Total Profit')

    class Meta:
        model = SalesRecord
        import_id_fields = ('order_id',)
        fields = (
            'order_id', 'region', 'country', 'item_type', 'sales_channel',
            'order_priority', 'order_date', 'ship_date', 'units_sold',
            'unit_price', 'unit_cost', 'total_revenue', 'total_cost', 'total_profit'
        )

class SalesRecordAdmin(ImportExportModelAdmin):
    resource_class = SalesRecordResource
    list_display = ('order_id', 'region', 'country', 'item_type', 'units_sold')
    search_fields = ('order_id', 'country', 'item_type')
    list_filter = ('region', 'country', 'item_type')

admin.site.register(SalesRecord, SalesRecordAdmin)
