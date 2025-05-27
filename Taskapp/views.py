from django.http import HttpResponse
import csv
from django.shortcuts import render, get_object_or_404, redirect
from .models import SalesRecord
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import SalesRecordForm
from datetime import datetime

def sales_list(request):
    records = SalesRecord.objects.all()
    for i in records:
        if i.id ==3:
            print(i.order_date)
            print(i.ship_date)
            break
    

    region = request.GET.get('region')
    country = request.GET.get('country')
    item_type = request.GET.get('item_type')
    search = request.GET.get('search')

    if region:
        records = records.filter(region=region)
    if country:
        records = records.filter(country=country)
    if item_type:
        records = records.filter(item_type=item_type)
    if search:
        records = records.filter(
            Q(order_id__icontains=search) |
            Q(country__icontains=search) |
            Q(item_type__icontains=search)|
            Q(region__icontains=search) |
            Q(sales_channel__icontains=search)|
            Q(order_priority__icontains=search)|
            Q(order_date__icontains=search)|
            Q(ship_date__icontains=search)|
            Q(units_sold__icontains=search)|
            Q(unit_price__icontains=search)|
            Q(total_profit__icontains=search)
        )

    paginator = Paginator(records, 500)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    # print(page_obj)
    # print(page_obj.object_list)

    context = {
        'page_obj': page_obj,
        'regions': SalesRecord.objects.values_list('region', flat=True).distinct(),
        'countries': SalesRecord.objects.values_list('country', flat=True).distinct(),
        'item_types': SalesRecord.objects.values_list('item_type', flat=True).distinct(),
    }
    return render(request, 'Taskapp/sales_list.html', context)
    # return render(request, 'Taskapp/list1.html', context)

def sales_add(request):
    if request.method == 'POST':
        form = SalesRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesRecordForm()
    return render(request, 'Taskapp/sales_add.html', {'form': form})

def sales_edit(request, pk):
    record = get_object_or_404(SalesRecord, pk=pk)
    if request.method == 'POST':
        form = SalesRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('sales_list')
    else:
        form = SalesRecordForm(instance=record)
    return render(request, 'Taskapp/sales_edit.html', {'form': form, 'record': record})

def Download_sales_csv(request):
    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="sales_records.csv"'
    data = csv.writer(response)

    data.writerow([
        'Sl No', 'Region', 'Country', 'Item Type', 'Sales Channel',
        'Order Priority', 'Order Date', 'Order ID', 'Ship Date',
        'Units Sold', 'Unit Price', 'Unit Cost', 'Total Revenue',
        'Total Cost', 'Total Profit'
    ])

    for record in SalesRecord.objects.all():
        order_date = f'="{record.order_date.strftime("%d/%m/%Y")}"'
        ship_date = f'="{record.ship_date.strftime("%d/%m/%Y")}"'

        data.writerow([
            record.id,
            record.region,
            record.country,
            record.item_type,
            record.sales_channel,
            record.order_priority,
            order_date,
            record.order_id,
            ship_date,
            record.units_sold,
            record.unit_price,
            record.unit_cost,
            record.total_revenue,
            record.total_cost,
            record.total_profit
        ])

    return response

def clean_date(date_str):
    """Cleans and parses date strings like ='31/08/2015'."""
    date_str = date_str.strip().replace('="', '').replace('"', '')
    return datetime.strptime(date_str, "%d/%m/%Y").date()

def import_sales_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            return render(request, 'import.html', {'error': 'Please upload a CSV file.'})

        try:
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)

            for row in reader:
                SalesRecord.objects.create(
                    region=row['Region'].strip(),
                    country=row['Country'].strip(),
                    item_type=row['Item Type'].strip(),
                    sales_channel=row['Sales Channel'].strip(),
                    order_priority=row['Order Priority'].strip(),
                    order_date=clean_date(row['Order Date']),
                    order_id=int(row['Order ID'].strip().replace('"', '').replace('=', '')),
                    ship_date=clean_date(row['Ship Date']),
                    units_sold=int(row['Units Sold']),
                    unit_price=float(row['Unit Price']),
                    unit_cost=float(row['Unit Cost']),
                    total_revenue=float(row['Total Revenue']),
                    total_cost=float(row['Total Cost']),
                    total_profit=float(row['Total Profit']),
                )
            return render(request, 'Taskapp/import_csv.html', {'message': 'CSV file uploaded successfully!'})

        except Exception as e:
            return render(request, 'Taskapp/import_csv.html', {'error': f'Error processing file: {e}'})

    return render(request, 'Taskapp/import_csv.html')
