# True Tarot

> Инновационный инструмент для рекрутеров, который позволяет оценивать совместимость между коллегами, руководителями и
> подчиненными или то, насколько кандидат подходит данной компании.

### Функционал MVP:

- Регистрация личного аккаунта для hr, а также дополнительно сброс/восстановление/подтверждение пароля
- Заполнение и сохранение анкет о работниках и кандидатах
- Просмотр списка сохраненных анкет, удаление анкет
- Выбор варианта просмотра совместимости - между кандидатом и сотрудником/командой сотрудников
- Выбор дополнительных опций, которые будут влиять на дополнительные карты в раскладе
- Выбор старших арканов и придворных карт в качестве сигнификатора для кверентов
- Просмотр результатов по сигнификаторам кверентов и дополнительным картам

### Идеи для будущей разработки:

- Сохранение результатов раскладов
- Сохранение результатов в отдельный файл
- Генерация файла-анкеты для кандидата (чтобы hr не заполнял самостоятельно)
- Использование для анализа различные астрологические направления (натальная, предсказательная, синастрическая)
- Улучшение алгоритм анализа сигнификатора для кверента
- Добавление дополнительных опций, которые будут влиять на выбор карт во время расклада
- Обратная связь за неделю/месяц: на основе сделанных раскладов система формирует персонализированную обратную связь,
  предлагая конкретные действия для повышения эффективности.
- Развитие soft skills
- и др.

### Алгоритм выбора сигнификатора для кверентов

> При заполнении анкеты о сотруднике/кандидате запрашивается его дата рождения.
> По дате рождения вычисляется возраст, солнечный знак и два сигнификатора. В дальнейшем можно выбрать какой из
> сигнификаторов использовать в анализе совместимости.
> Первый сигнификатор определяется старшим арканом по дате рождения: все цифры складываются между собой до тех пор, пока
> не получится число в промежутке от 0 до 22 (22 - количество старших арканов).
> Второй сигнификатор определяется придворными картами.
> По дате рождения вычисляется солнечный знак и возраст, что в дальнейшем используется для определения конкретной
> придворной карты.
> Используется логика распределения знаком зодиака между мастями колоды. Стоит сделать примечание про возраст - не
> всегда "Паж" обозначает именно юношу, это обозначение также может выпасть и на девушку.

# Инструкция по запуску проекта в dev режиме

### Склонируйте репозиторий с помощью git команды:

```
git clone git@github.com:ArtemHelloWorld/hackaton_naimix.git
```

### Создайте виртуальное окружение и активируйте его:

```
python3 -m venv venv 
```

```
source venv/bin/activate 
```

### Установить зависимости:

```
pip3 install -r requirements.txt
```

### Переменные виртуального окружения

> Создайте в корневой директории проекта файл `.env`. Заполните файл переменными
> окружения по примеру файла `env.example`, расположенный также в корневой
> директории проекта.

> Значение переменной DJANGO_DEBUG в прод режиме False, в дев режиме True. От
> этого значения зависит отображение данных на страницах.

### Перейдите в другую директорию:

```commandline
cd project
```

### Получить данные секретного ключа для проекта можно с помощью выполнения следующих команд в терминале:

```
python3 manage.py shell
```

```
from django.core.management.utils import get_random_secret_key
```

```
get_random_secret_key()
```

### Выполните миграции для создания таблиц в БД:

```
python3 manage.py migrate
```

### Создайте пользователя для входа в admin-панель:

```
python3 manage.py createsuperuser
```

> После выполнения команды заполните все нужные поля в консоли (юзернейм, почта, пароль)

### Запустите проект с помощью следующей команды и перейдите по ссылке в терминале:

```
python3 manage.py runserver
```
