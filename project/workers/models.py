import json

from django.db import models
from django.utils import timezone


class Employee(models.Model):
    class StatusChoices(models.TextChoices):
        CANDIDATE = ("CA", "Кандидат")
        WORKER = ("WR", "Сотрудник")

    is_candidate = models.CharField(
        max_length=2,
        help_text="Статус",
        choices=StatusChoices.choices,
        default=StatusChoices.CANDIDATE,
    )
    first_name = models.CharField(
        max_length=50,
        help_text="Имя",
        verbose_name="Иван",
    )
    last_name = models.CharField(
        max_length=50,
        help_text="Фамилия",
        verbose_name="Иванов",
    )
    location = models.CharField(
        max_length=50,
        help_text="Город/населенный пункт",
        verbose_name='Москва'
    )
    email = models.EmailField(
        max_length=100,
        help_text="Электронный адрес",
        verbose_name='mail@example.com'
    )
    phone = models.CharField(
        max_length=15,
        help_text="Номер телефона",
        verbose_name='+7 999 999 99 99'
    )
    general_skills = models.TextField(
        help_text="Основные навыки",
        verbose_name='Укажите основные навыки'
    )
    birthday = models.DateField(
        help_text="Дата рождения",
        verbose_name="Дата рождения",
    )
    zodiac_sign = models.CharField(
        max_length=15,
        help_text="Знак зодиака",
        verbose_name="Знак зодиака",
    )
    age = models.IntegerField(
        help_text="Возраст",
        verbose_name="Возраст",
    )
    significator = models.IntegerField(
        help_text="Сигнификатор",
        verbose_name="Сигнификатор",
    )
    court_card = models.IntegerField(
        help_text="Придворная карта",
        verbose_name="Придворная карта",
    )

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        birthday = self.birthday
        age = today.year - birthday.year - (
                (today.month, today.day) < (birthday.month, birthday.day)
        )
        self.age = age

        def get_zodiac_sign(birthday):
            zodiac_signs = [
                ((1, 20), 'Козерог'),
                ((2, 19), 'Водолей'),
                ((3, 21), 'Рыбы'),
                ((4, 20), 'Овен'),
                ((5, 21), 'Телец'),
                ((6, 21), 'Близнецы'),
                ((7, 23), 'Рак'),
                ((8, 23), 'Лев'),
                ((9, 23), 'Дева'),
                ((10, 23), 'Весы'),
                ((11, 22), 'Скорпион'),
                ((12, 22), 'Стрелец'),
                ((12, 31), 'Козерог'),
            ]
            birth_month = birthday.month
            birth_day = birthday.day
            for date, sign in zodiac_signs:
                if (birth_month, birth_day) <= date:
                    return sign
            return 'Козерог'

        self.zodiac_sign = get_zodiac_sign(self.birthday)

        date_str = self.birthday.strftime('%d%m%Y')
        total = sum(int(digit) for digit in date_str if digit.isdigit())
        while total > 22:
            total -= 22
        self.significator = total

        def court_card_f(age, sign):
            with open('../cards.json', 'r', encoding='utf-8') as js_file:
                cards = json.load(js_file)
                for card in cards:
                    if (card["type"] == "Придворная карта"
                            and sign in card["zodiac_sign"]
                            and card["age"][0] <= age <= card["age"][1]):
                        print(card)
                        return card["card_id"]
                return 0

        self.court_card = court_card_f(self.age, self.zodiac_sign)

        super().save(*args, **kwargs)
