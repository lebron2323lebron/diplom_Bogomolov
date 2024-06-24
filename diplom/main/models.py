from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator

from users.models import User, Profile


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, verbose_name="название")
    logo = models.ImageField(verbose_name="логотип", null=True, blank=True)
    users = models.ManyToManyField(get_user_model(), related_name="courses", null=True)

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.title


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
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="participation_applications")
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


class Zakaz(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.ManyToManyField(get_user_model(), related_name="zakaz", null=True)
    # created = models.DateTimeField( auto_now_add=True)
    # updated = models.DateTimeField(auto_now_add=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=False, verbose_name='Номер телефона')
    kater = models.ImageField(verbose_name='катер', null=True, blank=True)
    usluga = models.ForeignKey(Uslugs, on_delete=models.CASCADE, verbose_name='Вид услуги', related_name='zakazuslugi')
    kolichestvo = models.IntegerField(null=False, blank=False, verbose_name='Количество участников')
    komment = models.CharField(max_length=255, verbose_name='Комментарий')

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

