# forms.py
from django import forms

class SearchForm(forms.Form):
    
    search_query = forms.CharField(label='Search by Location', max_length=100, required=False)
    rate = forms.ChoiceField(
        label='Select Rating',
        choices=[
            (0, 'Select'),
            (5, '4.0 - 5.0'),
            (4, '3.0 - 4.0'),
            (3, '2.0 - 3.0'),
            (2, '1.0 - 2.0'),
            (1, '0.0 - 1.0'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control custom-select'}),
    )
    online_order = forms.ChoiceField(
        label='Select online order',
        choices=[
            (0, 'Select'),
            (1, 'Yes'),
            (2, 'No'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control custom-select'}),
    )
    book_table = forms.ChoiceField(
        label='Select book table',
        choices=[
            (0, 'Select'),
            (1, 'Yes'),
            (2, 'No'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control custom-select'}),
    )

    listed_in_type = forms.ChoiceField(
        label='Select Type',
        choices=[
            (None, 'Select'),
            ("Buffet", 'Buffet'),
            ("Delivery", 'Delivery'),
            ("Dine-out", 'Dine-out'),
            ("Desserts", 'Desserts'),
            ("Cafes", 'Cafes'),
            ("Drinks & nightlife", 'Drinks & nightlife'),
            ("Pubs and bars", 'Pubs and bars'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control custom-select'}),
    )