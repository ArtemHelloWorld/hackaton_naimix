import django.contrib.auth.models
import django.db.models


class User(django.contrib.auth.models.AbstractUser):
    image = django.db.models.ImageField(
        upload_to='profile_image/%Y/%m/%d',
        null=True,
        blank=True,
        verbose_name='аватарка',
    )

    birthday = django.db.models.DateField(
        null=True, blank=True, verbose_name='дата рождения'
    )


    def __str__(self):
        return f'Пользователь {self.pk}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
