# Аутентификация и авторизация. Протокол OAuth 2.0

### Задание

В index.html добавить возможность авторизации через какой-либо сервис (например “Авторизация через Google”) по аналогии с авторизацией VK.

• Для проверки домашнего задания приложи:
 - скриншот с кнопками авторизации,
 - скриншот авторизации через внешний сервер,
 - скриншот страницы с успешной авторизацией, 
 - скриншот из Django-admin, где помимо администратора есть как минимум 2 учетных записи

### Настройка виртуального окружения
Виртуальное окружение настраивается по аналогии с описанием из [репозитория](https://github.com/selvnv/py-setup)

#### Зависимости: 
* Основные:
  * `django`
  * `social-auth-app-django`

Активация виртуальной среды (Windows): `.\.venv\Scripts\activate`

Создание проекта в корневой директории: `django-admin startproject oauth .`

Создание сервиса: `py .\manage.py startapp auth_service`

#### Регистрация сервисов:
```python
# settings.py
INSTALLED_APPS = (
    # ...
    'social_django',
    'auth_service',
    # ...
)
```

#### Регистрация шаблонов
```python
# settings.py
TEMPLATES = [
    {
        # ...
        'OPTIONS': {
            # ...
            'context_processors': [
                # ...
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                # ...
            ]
        }
    }
]
```

#### Добавление настроек аутентификации

```python
# settings.py
AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.vk.VKOAuth2'
    # ...
    'django.contrib.auth.backends.ModelBackend',
)
```

#### Настройки интеграции со сторонними сервисами

```python

```

#### Регистрация маршрутов
```python
# auth_service/urls
from django.urls import path, include

from auth_service.views import index

urlpatterns = [
    path('auth/', index, name='index'),
    path('auth/social/', include('social_django.urls', namespace='social'))
]

# oauth/urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_service.urls'))
]
```

### Запуск

Выполнение миграций: `py .\manage.py migrate `

Запуск сервера: ` py .\manage.py runserver`

