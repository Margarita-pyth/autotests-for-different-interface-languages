# Запуск автотестов для разных языков интерфейса
## _Selenium_

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

В рамках курса "Автоматизация тестирования с помощью Selenium и Python".
(https://stepik.org/course/575)

- ✨Magic ✨Python

## Предусловия
- Использовался интепритатор Python3
- Склонируйте репозиторий
- Создайте и активируйте виртуальное окружение
- Установите PYTEST командой: pip install pytest==7.1.2
- Установите SELENIUM командой: pip install selenium==4.* (проверка установки: pip list)
- Установите драйвер для браузера  
- - Chrome: chromedriver: https://sites.google.com/chromium.org/driver/
- - Firefox: geckodriver: https://github.com/mozilla/geckodriver/releases
- Добавьте путь к драйверу - в системную переменную PATH (в настройках системы вашего ПК).
- 
## Запуск скрипта
- Запустите скрипт в консоли командой:
- -  pytest --browser_name=firefox --language=ru test_items.py  - для выполнения скрипта в браузере Firefox,
- - pytest --browser_name=chrome --language=en test_items.py - для выполнения скрипта в браузере Chrome.
- Можно выставить любой язык отображения страницы через "--language=en"
