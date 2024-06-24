from django import forms
from phonenumber_field.formfields import PhoneNumberField

from main.models import ParticipationApplication, Course, Uslugs, Zakaz


class ApplicationForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    course = forms.ModelChoiceField(queryset=Course.objects.all())

    class Meta:
        model = ParticipationApplication
        fields = ("course", "phone_number", "price", "date", "time", "wishes")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
            "time": forms.TimeInput(attrs={"type": "time"})
        }


class ZakazForm(forms.ModelForm):
    created = forms.DateTimeField(label="Время создания")
    users = forms.CharField(label='Пользователь') 
    class Meta:
        model = Zakaz
        fields = '__all__'
        exclude = ['id','kater']
        # labels = {
        #     'first_name': 'Имя',
        #     'last_name': 'Фамилия',
        #     'updated': 'Дата обработки',
        #     'kater': 'Вид катера',
        # }
