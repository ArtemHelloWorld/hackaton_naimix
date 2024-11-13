import django.contrib.auth.models
import django.db.models
from django.core.validators import MaxValueValidator, MinValueValidator



class User(django.contrib.auth.models.AbstractUser):
    email = django.db.models.EmailField(
        null=True,
        blank=True,
        verbose_name='почта'
    )
    position = django.db.models.CharField(
        default='Сотрудник',
        max_length=50,
        verbose_name='должность'
    )
    date_of_hiring = django.db.models.DateField(
        auto_now_add=True,
        null=True,
        blank=True,
        verbose_name='дата найма'
    )
    achievements = django.db.models.ManyToManyField(
        'Achievement',
        related_name='users'
    )
    profile_image = django.db.models.ImageField(
        upload_to='profile_images/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='фотография',
    )

    def __str__(self):
        return f'Пользователь {self.pk}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-date_of_hiring', 'id']


class Skill(django.db.models.Model):
    user = django.db.models.ForeignKey(
        User,
        on_delete=django.db.models.CASCADE,
        related_name='skills'
    )
    name = django.db.models.CharField(
        max_length=50,
        verbose_name='название'
    )
    rate = django.db.models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

class Achievement(django.db.models.Model):
    name = django.db.models.CharField(
        max_length=50,
        verbose_name='название'
    )
    description = django.db.models.CharField(
        max_length=150,
        verbose_name='описание'
    )
    image = django.db.models.ImageField(
        upload_to='acheivements/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='фотография',
    )