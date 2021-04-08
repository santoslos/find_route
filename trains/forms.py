from django import forms

from trains.models import Train


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'placeholder': 'Ввидите название города '}))

    class Meta:
        model = Train
        fields = ('name',)