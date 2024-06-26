from django import forms

from main.models import ParticipationApplication, Uslugs, Zakaz, Remont, Zapros


class ZakazForm(forms.ModelForm):
    created = forms.DateTimeField(label="Время создания")
    class Meta:
        model = Zakaz
        fields = '__all__'
        exclude = ['id','kater','users']
        # labels = {
        #     'first_name': 'Имя',
        #     'last_name': 'Фамилия',
        #     'updated': 'Дата обработки',
        #     'kater': 'Вид катера',
        # }

class RemontForm(forms.ModelForm):
    class Meta:
        model = Remont
        fields = ['mehanik', 'data', 'usluga', 'kater']


class ZaprosForm(forms.ModelForm):
    class Meta:
        model = Zapros
        fields = ['name', 'phone_number', 'title']