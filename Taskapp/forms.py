from django import forms
from .models import SalesRecord

class SalesRecordForm(forms.ModelForm):
    order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ship_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(SalesRecordForm, self).__init__(*args, **kwargs)
        self.fields['region'].widget = forms.Select(choices=[(r['region'], r['region']) for r in SalesRecord.objects.values('region').distinct()])
        self.fields['country'].widget = forms.Select(choices=[(r['country'], r['country']) for r in SalesRecord.objects.values('country').distinct()])
        self.fields['item_type'].widget = forms.Select(choices=[(r['item_type'], r['item_type']) for r in SalesRecord.objects.values('item_type').distinct()])

    class Meta:
        model = SalesRecord
        fields = '__all__'
