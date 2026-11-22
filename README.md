# UI-тесты Stellar Burgers

17 сценариев запускаются в Chrome и Firefox. Каждый запуск использует отдельный профиль браузера. Стенд — `https://qa-stellarburgers.education-services.ru`.

| Раздел | Сценарии на один браузер |
| --- | ---: |
| Восстановление пароля | 3 |
| Личный кабинет | 3 |
| Конструктор и навигация | 6 |
| Лента заказов | 5 |

Классы страниц находятся в `pages/`, локаторы — в `locators.py`, тесты и фикстуры — в `tests/`. Фикстуры регистрируют временных пользователей через API и удаляют их после теста. Оформление в конструкторе проверяется через интерфейс. Для проверок ленты заказы создаются через API. В документации стенда нет операции удаления заказов.

## Запуск

Требуются установленные Chrome и Firefox. Selenium Manager подбирает драйвер для каждого браузера. Для генерации автономного HTML-отчёта требуется Allure CLI 2 с поддержкой `--single-file`.

```sh
python3 -m pip install -r requirements.txt
python3 -m pytest -q --alluredir=allure-results --clean-alluredir
allure generate allure-results --clean --single-file -o allure-report
```

Готовый отчёт можно открыть в браузере из `allure-report/index.html`. Для запуска в одном браузере используйте `python3 -m pytest -k chrome` или `python3 -m pytest -k firefox`.
