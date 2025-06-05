from django.test import TestCase
from django.urls import reverse
from .models import SalesRecord
from datetime import date

class SalesListViewTests(TestCase):
    def setUp(self):
        # Create sample records
        SalesRecord.objects.create(
            order_id='A001',
            region='Asia',
            country='India',
            item_type='Clothes',
            sales_channel='Online',
            order_priority='H',
            order_date=date(2024, 1, 10),
            ship_date=date(2024, 1, 15),
            units_sold=100,
            unit_price=20.00,
            total_profit=2000.00
        )
        SalesRecord.objects.create(
            order_id='A002',
            region='Europe',
            country='Germany',
            item_type='Beverages',
            sales_channel='Offline',
            order_priority='M',
            order_date=date(2024, 2, 5),
            ship_date=date(2024, 2, 10),
            units_sold=50,
            unit_price=10.00,
            total_profit=500.00
        )

    def test_sales_list_loads_successfully(self):
        response = self.client.get(reverse('sales_list'))  # change to your actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Taskapp/sales_list.html')
        self.assertContains(response, 'Sales Records')

    def test_filter_by_region(self):
        response = self.client.get(reverse('sales_list'), {'region': 'Asia'})
        self.assertEqual(len(response.context['page_obj']), 1)
        self.assertContains(response, 'India')

    def test_filter_by_country(self):
        response = self.client.get(reverse('sales_list'), {'country': 'Germany'})
        self.assertEqual(len(response.context['page_obj']), 1)
        self.assertContains(response, 'Germany')

    def test_search(self):
        response = self.client.get(reverse('sales_list'), {'search': 'A002'})
        self.assertEqual(len(response.context['page_obj']), 1)
        self.assertContains(response, 'Germany')

    def test_pagination(self):
        # Create more records to test pagination
        for i in range(600):
            SalesRecord.objects.create(
                order_id=f'ORD{i}',
                region='Asia',
                country='India',
                item_type='Clothes',
                sales_channel='Online',
                order_priority='H',
                order_date=date(2024, 3, 1),
                ship_date=date(2024, 3, 2),
                units_sold=1,
                unit_price=1.00,
                total_profit=1.00
            )

        response = self.client.get(reverse('sales_list'))
        self.assertTrue('page_obj' in response.context)
        self.assertEqual(len(response.context['page_obj']), 500)  # first page has 500
