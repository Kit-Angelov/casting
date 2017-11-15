from django.db import models
# from django_countries.fields import CountryField
# from cities.models import BaseCountry


class HairColor(models.Model):
    """
        Цвет волос
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    """
        Город
    """
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Gender(models.Model):
    """
        Пол
    """
    name = models.CharField(max_length=20)
    id_c = models.IntegerField()

    def __str__(self):
        return self.name


class Country(models.Model):
    """
        Страна
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class EyeColor(models.Model):
    """
        Цвет глаз
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class AppearanceType(models.Model):
    """
        Тип внешности
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class EmploymentType(models.Model):
    """
        Тип наемнного рабочего
    """
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    original = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Parameters(models.Model):
    """
        Класс Параметры - список основных параметров Наемника + используется в определнии требований Роли
    """
    age = models.IntegerField(verbose_name='Возраст')
    growth = models.IntegerField(verbose_name='Рост в сантиметрах')
    clothsize = models.IntegerField(verbose_name='Размер одежды (40, 43, 48..)')
    chestsize = models.IntegerField(verbose_name='Обхват груди в сантиметрах')
    waistsize = models.IntegerField(verbose_name='Обхват талии в сантиметрах')
    thighsize = models.IntegerField(verbose_name='Обхват бедер в сантиемтрах')
    footsize = models.IntegerField(verbose_name='Размер обуви')
    necksize = models.IntegerField(blank=True, null=True, verbose_name='Обхват шеи в сантиметрах')
    headsize = models.IntegerField(blank=True, null=True, verbose_name='Обхват головы в сантиметрах')
    tatu = models.BooleanField(default=False, verbose_name='Наличие татуировок')
    piercing = models.BooleanField(default=False, verbose_name='Наличие пирсинга')
    appearancetype = models.ForeignKey(AppearanceType, on_delete=models.CASCADE)
    haircolor = models.ForeignKey(HairColor, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    employmenttype = models.ManyToManyField(EmploymentType, blank=True)
    eyecolor = models.ForeignKey(EyeColor, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Contacts(models.Model):
    """

    """
    email = models.CharField(max_length=30, verbose_name='Мыло')
    phone_number = models.CharField(max_length=30, verbose_name='Мобилка')
    email_img = models.ImageField(null=True, blank=True, verbose_name='')
    phone_number_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return '{0}, {1}'.format(self.email, self.phone_number)


class Employee(models.Model):
    """
        Наемник
    """
    firstname = models.CharField(max_length=20, verbose_name='Фамилия')
    lastname = models.CharField(max_length=20, verbose_name='Имя')
    photo = models.ImageField(blank=True, null=True)
    param_list = models.OneToOneField(Parameters, on_delete=models.CASCADE)
    contacts = models.OneToOneField(Contacts, on_delete=models.CASCADE, blank=True, null=True)
    professional_rating = models.FloatField(verbose_name='Рейтинг проф навыков')
    human_rating = models.FloatField(verbose_name='Рейтинг человеческих качеств')

    @property
    def professional_rating(self):
        prof_rating = 0
        if self.Review_set is not None:
            for rat in self.Review_set:
                prof_rating += rat.professional_rating
            prof_rating /= len(self.Review_set)
        return prof_rating

    @property
    def human_rating(self):
        hum_rating = 0
        if self.Review_set is not None:
            for rat in self.Review_set:
                hum_rating += rat.professional_rating
            hum_rating /= len(self.Review_set)
        return hum_rating

    def __str__(self):
        return '{0}, {1}'.format(self.firstname, self.lastname)


class PortfolioElem(models.Model):
    """
        Элемент портфолио
    """
    name = models.CharField(max_length=20)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField(max_length=1000)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employer(models.Model):
    """
        Наниматель
    """
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)

    def __str__(self):
        return self.firstname


class CastingType(models.Model):
    """
        Вид кастинга
    """
    original = models.BooleanField(default=True)
    name = models.CharField(max_length=20)
    info = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
        Оплата
    """
    name = models.CharField(max_length=20, verbose_name='Наименование')
    amount = models.FloatField()
    start_date = models.DateField()
    finish_date = models.DateField()
    emp = models.ForeignKey(Employer)

    def __str__(self):
        return self.name


class Casting(models.Model):
    """
        Кастинг
    """
    name = models.CharField(max_length=20)
    image = models.ImageField()
    description = models.TextField(max_length=1000)
    type = models.ForeignKey(CastingType)
    owner = models.ForeignKey(Employee)

    def __str__(self):
        return self.name


class Role(models.Model):
    """
        Роль
    """
    name = models.CharField(max_length=20)
    salary = models.FloatField()
    start_date = models.DateField()
    expire_date = models.DateField()
    casting = models.ForeignKey(Casting)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class RequestStatus(models.Model):
    name = models.CharField(max_length=10)
    status_id = models.IntegerField()

    def __str__(self):
        return self.name


class Request(models.Model):
    """
        Заявка на роль
    """
    creation_date = models.DateField()
    role = models.ForeignKey(Role)
    employee = models.ForeignKey(Employee)
    status = models.ForeignKey(RequestStatus, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)


class Invite(models.Model):
    """
        Приглашение на роль
    """
    creation_date = models.DateField()
    employee = models.OneToOneField(Employee)
    creator = models.ForeignKey(Employer)
    role = models.OneToOneField(Role)

    def __str__(self):
        return str(self.pk)


class Review(models.Model):
    """
        Отзыв (?? меняет рейтинг актера ??)
    """
    professional_skills = models.IntegerField(choices={(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')})
    human_skills = models.IntegerField(choices={(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')})
    comments = models.TextField(max_length=1000, blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
