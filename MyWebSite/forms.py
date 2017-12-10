from django import forms


CITIES = ( ('TEL - Aviv', 'Tel Aviv'), ('Jerusalem', 'Jerusalem')       )

class MyForm(forms.Form):
    name = forms.CharField(label = 'Name :')
    city = forms.ChoiceField(label = 'City', choices=CITIES, widget = forms.RadioSelect())


