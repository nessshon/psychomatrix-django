from django import forms
from datetime import datetime


class DateInputForm(forms.Form):
    date = forms.DateField(
        required=True,
        label='Выберите дату рождения:',
        widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'datepicker'},
        ),
        initial=datetime.today().strftime('%Y-%m-%d'),
    )
