![Title PNG "Skill Factory"](https://user-images.githubusercontent.com/82756474/145072620-c7947355-bea9-4f61-ba7c-e7db5e0cff6a.png)


# Проект №6. Car Price prediction

<!-- vim-markdown-toc Redcarpet -->

* [Задача](#задача)
    * [Краткое описание](#краткое-описание)
    * [Детали реализации](#детали-реализации)
* [Структура репозитория](#структура-репозитория)

<!-- vim-markdown-toc -->

Проект выполнил: Sergey Derevyanov

Дата завершения проекта: 09.12.2021

Группа: group_dspr-44

Логин на kaggle.com: sergeyderevyanov

Ссылка на работу kaggle.com: https://www.kaggle.com/sergeyderevyanov/derevyanov-s-sf-dst-car-price-prediction

Оценка на ЛБ: 15.37946

[Отчетный ноутбук](https://github.com/Sergder717/Skillfactory_rds/blob/main/module_6/derevyanov-s-sf-dst-car-price-prediction.ipynb)

## Задача

https://www.kaggle.com/c/sf-dst-car-price-prediction


### Краткое описание

Цель проекта: Предсказать стоимость автомобиля по его характеристикам.

Рамки проекта:
* Разрешено использовать внешние данные. (но их источник должен быть публичным и доступен всем участникам соревнования)
* Разрешено использовать любые ML алгоритмы и библиотеки. (кроме DL)
* Основная мертрика модели: MAPE (Mean Absolute Percentage Error). 

### Детали реализации

1. Разработан парсер данных с сайта auto.ru
2. Парсинг данных по брендам : 'SKODA', 'AUDI', 'HONDA', 'VOLVO', 'BMW', 'NISSAN', 'INFINITI',
'MERCEDES', 'TOYOTA', 'LEXUS', 'VOLKSWAGEN', 'MITSUBISHI'. В итоге была собрана информация по 113074 авто.
Сформированы следующие файлы формата .csv:
    * auto_ru_data_skoda.csv
    * auto_ru_data_audi.csv
    * auto_ru_data_honda.csv
    * auto_ru_data_volvo.csv
    * auto_ru_data_bmw.csv
    * auto_ru_data_nissan.csv
    * auto_ru_data_infiniti.csv
    * auto_ru_data_mercedes.csv
    * auto_ru_data_toyota.csv
    * auto_ru_data_volkswagen.csv
    * auto_ru_data_mitsubishi.csv 
    * auto_ru_data_rare.csv
3. Произведена предобработка данных
4. Сделан Разведочный анализ данных (EDA)
5. Созданы новые признаки (Feature engineering)
6. Сделано преобразование данных (Lable encoding)
7. Определены основные признаки для обучения
8. Создана модель 1. "Наивная" модель
9. Создана модель 2. CatBoost
10. Создана модель 3. RandomForest
11. Создана модель 4. ExtraTreesRegressor
12. Создана модель 5. XGBRegressor
13. Сделан Stacking

## Структура репозитория

В корневой папке находятся все файлы:

- Файл derevyanov-s-sf-dst-car-price-prediction.ipynb - ноутбук с решением проекта https://github.com/Sergder717/Skillfactory_rds/blob/main/module_6/derevyanov-s-sf-dst-car-price-prediction.ipynb
- Папка auto_ru_parsing_12_2021 - файлы с данными, собранные парсером https://github.com/Sergder717/Skillfactory_rds/tree/main/module_6/auto_ru_parsing_12_2021
- Parser.py - код парсера https://github.com/Sergder717/Skillfactory_rds/blob/main/module_6/Parser.py
- test.zip - тестовый датасет https://github.com/Sergder717/Skillfactory_rds/blob/main/module_6/test.zip

