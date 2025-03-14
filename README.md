# technostrelka_infomotion
При запуске решения открывается веб страница с логотипами ИнфоМоушен и поисковой строкой. Пользователь может найти фильм по названию или по тэгу.

Список зависимостей:

BeautifulSoup — это библиотека Python для извлечения данных из HTML и XML

Requests — это библиотека для выполнения HTTP-запросов на языке Python

Dataclasses в Python — это способ автоматизировать генерацию кода классов, ориентированных на хранение данных. Они позволяют значительно сократить шаблонный код классов

lib2to3.fixes.fix_input — это фиксатор для преобразования ввода в библиотеке 2to3.

django.core.paginator — это модуль в Django, который предоставляет встроенный класс Paginator для поддержки пагинации. 
Класс принимает два аргумента: список объектов для пагинации и количество объектов, которые нужно отображать на странице.

tkinter.font — встроенный модуль в библиотеке Tkinter для работы со шрифтами. Он позволяет задавать размер, семейство, стиль и другие параметры текста для различных виджетов

Django REST Framework (DRF) — это набор инструментов для создания веб-сервисов и API на основе фреймворка Django

django.contrib.admin.templatetags.admin_list— это модуль в Django, который содержит различные функции для работы с листами изменений в административной части

Django shortcuts — это модуль с коллекцией вспомогательных функций, которые помогают ускорить процесс разработки.

Модуль os в Python — это часть стандартной библиотеки, которая предоставляет кросс-платформенные функции для работы с операционной системой.
Он позволяет осуществлять управление файлами, директориями, процессами и многое другое

re в Python — это модуль для работы с регулярными выражениями. Он предоставляет инструменты для поиска, замены и деления текста на основе паттернов или шаблонов.

django.contrib — это пакет в веб-фреймворке Django, который содержит дополнительные необязательные инструменты для решения распространённых проблем веб-разработки.

django.urls — это пакет в Python, который позволяет сопоставлять URL-адреса с функциями-представлениями в Django.
Функция path() в этом пакете принимает четыре параметра:
 1 route — шаблон адреса URL, которому должен соответствовать запрос;
 2 view — функция-представление, которое обрабатывает запрос;
 3 kwargs — дополнительные аргументы, которые передаются в функцию-представление; 
 4 name — название маршрута.

 django.views.generic.base — это модуль, который содержит встроенные представления для общих задач в Django. В нашем проекте мы использовали класс View. Базовый класс представления, от которого наследуются все другие представления-классы.

 django.db — это модуль для работы с базами данных в Django. Он позволяет настраивать подключение к различным базам данных, таким как PostgreSQL, MySQL, SQLite и Oracle.

 Модуль django.db.models в Django используется для создания и управления схемой базы данных.
 
Алгоритм запуска программы:
Вам необходимо скачать архив kinopoisk (8).zip на компьютер. Откройте любой редактор кода, например: PyCharm, VS Code и другие. После этого зайдите в поле Terminal и скачайте нужные библиотеки с помощью команд:


pip install django

pip install requests

pip install beautifulsoup4

pip install djangorestframework

python -m pip install Pillow


Далее введите в терминал следующие строки:

cd kinopoisk

python manage.py runserver

Далее переходите по появившейся в терминале ссылке. Вам откроется сайт ИнфоМоушен, на котором Вы можете посмотреть собранную базу фильмов. Также Вы можете воспользоваться поиском и проверить работоспособность сайта и поисковой строки.
