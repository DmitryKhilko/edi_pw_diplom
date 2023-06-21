# Информация о проекте
Тестовый фреймворк для автоматизации тестирования автоматизированной 
информационной системы "EDI-Flow".
Тестовый фреймворк содержит UI-автотесты, API-автотесты.
Для запуска автотестов используется CI-система Jenkins.
В Jenkins выгрузка результата прогона автотестов происходит 
в систему управления тестирование Allure TestOps.  

## Инструкция по установке на локальном компьютере
Клонирование проекта из репозитория: 
git clone https://github.com/DmitryKhilko/edi_pw_diplom

Установка пакетов:
pip3 install -r requirements.txt

## Инструкция по запуску автотестов
Запуск всех автоестов:
pytest -v --reruns 2 -n auto --alluredir=allure-reports

Запуск выборочных автотестов с тегами smoke, critical_path, extended:
pytest -v -m smoke --reruns 2 -n auto --alluredir=allure-reports
pytest -v -m critical_path --reruns 2 -n auto --alluredir=allure-reports
pytest -v -m extended  --reruns 2 -n auto --alluredir=allure-reports
pytest -v -m 'not extended'  --reruns 2 -n auto --alluredir=allure-reports

## Полезные гиперссылки
- https://docs.pytest.org
- https://docs-python.ru/packages/frejmvork-pytest/
- https://playwright.dev/python/docs/intro
 