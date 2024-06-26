from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

from users.models import User, Profile


class Uslugs(models.Model):
    title = models.CharField(max_length=255,null=False, blank=False, verbose_name="название")
    logo = models.ImageField(verbose_name="логотип", null=True, blank=True)
    users = models.ManyToManyField(get_user_model(), related_name="uslugs", null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title


class ParticipationApplication(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр в длину.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="participation_applications")
    price = models.DecimalField(max_digits=11, decimal_places=2)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')
    time = models.TimeField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    wishes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Заявка на участие"
        verbose_name_plural = "Заявки на участие"


class Reiting(models.Model):
    user = models.ManyToManyField(get_user_model(), related_name="reiting", null=True)
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="Отзыв")
    logo = models.ImageField(verbose_name="аватар", null=True, blank=True)
    date = models.DateField(blank=False, null=False)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

class Zaiavki(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Zayavka", verbose_name='Пользователь')
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')

    class Meta:
        verbose_name = "Заявка на сертификаты"
        verbose_name_plural = "Заявки на сертификат"

    
class Workers(models.Model):
    firstname = models.CharField(max_length=255, null=False, blank=False, verbose_name='Имя')
    lastname = models.CharField(max_length=255, null=False, blank=False, verbose_name='Фамилия')
    about = models.CharField(max_length=255, null=False, blank=False, verbose_name="Описание")
    role = models.CharField(max_length=255, null=False, blank=False, verbose_name='Должность')
    logo = models.ImageField( verbose_name='аватар', null=True, blank=True)

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудник"


class Kater(models.Model):
    title = models.CharField(max_length=255,null=False, blank=False, verbose_name="название")
    kater = models.ImageField(verbose_name='катер', null=True, blank=True)
    opisanie = models.CharField(max_length=1000,null=False, blank=False, verbose_name="Описание катера")
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Катер"
        verbose_name_plural = "Катеры"

class Zakaz(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ManyToManyField(get_user_model(), related_name="zakaz", null=True)
    # created = models.DateTimeField( auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    data = models.DateTimeField(blank=False, null=False, verbose_name='Дата заявки ')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона долже быть в формате: '+79998887799'. До 15 символов длиной.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')
    kater = models.ForeignKey(Kater, on_delete=models.CASCADE, verbose_name='катер', null=True, blank=True)
    usluga = models.ForeignKey(Uslugs, on_delete=models.CASCADE, verbose_name='Вид услуги', related_name='zakazuslugi')
    kolichestvo = models.IntegerField(null=False, blank=False, verbose_name='Количество участников')
    komment = models.CharField(max_length=255, verbose_name='Комментарий')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class Remont(models.Model):
    mehanik = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Mehanik', verbose_name='Механик')
    data = models.DateField(blank=False, null=False, verbose_name='Дата ремонта')
    usluga = models.CharField(max_length=255, blank=False, null=False, verbose_name='Описание ремонта')
    kater = models.ForeignKey(Kater, on_delete=models.CASCADE, verbose_name='Катер', related_name='vidkatera')

    class Meta:
        verbose_name = "Ремонт"
        verbose_name_plural = "Ремонты"

class Zapros(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Kandidat', verbose_name='Кандидат')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Номер телефона долже быть в формате: '+79998887799'. До 15 символов длиной.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="О себе")

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"