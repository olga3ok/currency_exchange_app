# Currency Exchange App

### Используемые технологии:
- Django
- API https://www.exchangerate-api.com/.

### Перед запуском выполните:
- Склонировать репозиторий в локальную директорию:
```
git clone git@github.com:olga3ok/currency_exchange_app.git
```
- Активация виртуального окружения и установка зависимостей из requirements.txt:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
```
cd currency_exchange_app
```
```
pip install -r requirements.txt
```
- В корне проекта создайте .env и задайте значения переменных:
```
SECRET_KEY=
SECRET_API= (api key exchangerate-api)

- Запуск:
```
python manage.py runserver
```
