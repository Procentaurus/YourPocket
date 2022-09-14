import django_filters
from django import forms


class ExpenseFilter(django_filters.FilterSet):
    CATEGORIES = (
        ('Home','Home'),
        ('Health','Health'),
        ('Entertainment','Entertainment'),
        ('Transport', 'Transport'),
        ('Taxes and Fees', 'Taxes and Fees'),
        ('Clothes', 'Clothes'),
        ('Food', 'Food'),
        ('Credits and loans', 'Credits and loans'),
        ('Others', 'Others'),
    )
    exp_cat = django_filters.ChoiceFilter(field_name='category',widget=forms.Select,
        choices=CATEGORIES)
    exp_s_date = django_filters.DateFilter(field_name="date_created", lookup_expr='gte',
        label='Later than', widget=forms.DateInput(format='%Y-%m-%d"', attrs={'type': 'date',}))
    exp_e_date = django_filters.DateFilter(field_name="date_created", lookup_expr='lte',
        label='Earlier than', widget=forms.DateInput(format='%Y-%m-%d"', attrs={'type': 'date',}))

class IncomeFilter(django_filters.FilterSet):
    CATEGORIES = (
        ('Salary', 'Salary'),
        ('Return on investment', 'Return on investment'),
        ('Selling goods', 'Selling goods'),
        ('Credits and loans', 'Credit and loans'),
        ('Rent / pension', 'Rent / pension'),
        ('Bonus / Award', 'Bonus / Award'),
        ('Gifts', 'Gifts'),
        ('Others', 'Others'),
    )
    inc_cat = django_filters.ChoiceFilter(field_name='category',widget=forms.Select,
        choices=CATEGORIES)
    inc_s_date = django_filters.DateFilter(field_name="date_created", lookup_expr='gte',
        label='Later than', widget=forms.DateInput(format='%Y-%m-%d"', attrs={'type': 'date'}))
    inc_e_date = django_filters.DateFilter(field_name="date_created", lookup_expr='lte',
        label='Earlier than', widget=forms.DateInput(format='%Y-%m-%d"', attrs={'type': 'date'}))