venv\Scripts\activate

pip install > requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

1) Регистрация 
POST
api/v1/auth/signup/

required: phone (str email (str) password (str) re_password (str)

2) Вход 
POST
api/v1/auth/login/

required: email (str) password (str)

Возвращает: токен (указывать в заголовоках)

3) Выход 
DELETE
api/v1/auth/login/

4) Каталог товаров 
GET
api/v1/goods/

5) Добавление товара в корзину 
POST
api/v1/goods/

required: goods (int) count (int)

6) Добавление рейтинга 
POST
api/v1/goods/

required: goods (int) rate (int) -> (1-5)
 
7) Весь рейтинг 
GET
api/v1/goods/

required: goods (id) rate (True)

8) Медитация

Просто таблицу создал, не знал как описать и что там нужно

9) Восстановление пароля

Ничего не сделал, тк по номеру нужно (если нужно, то по почте могу сделать)

10) Рулетка 

не сделал, только генерацию промокода, тк алгоритма нет

11) Отзыв

не сделал, но написал таблицу, если нужно, то добавлю

12) Данные о юзере 
GET
api/v1/profile/

required id (int)

13) Данные о юзере редактирование 
PUT
api/v1/profile/

required id (int) email (str) phone (str)

14) Вcе данные о товаре 
GET
api/v1/goods/

required: goods (id) rate (False)
