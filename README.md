Booker API Automation Tests
https://img.shields.io/badge/Python-3.8%252B-blue
https://img.shields.io/badge/Pytest-Testing%2520Framework-green
https://img.shields.io/badge/Allure-Reports-orange
https://img.shields.io/badge/API-Testing-lightgrey

Проект автоматизированного тестирования REST API для Booker API. Включает позитивные и негативные тест-кейсы с генерацией подробных Allure отчетов.

📋 Оглавление
Особенности

Предварительные требования

Установка

Запуск тестов

Структура проекта

Генерация отчетов

Маркеры тестов

Примеры тестов

Устранение проблем

✨ Особенности
✅ Полное покрытие API: Booking, Authentication, CRUD операции

🧪 Позитивные и негативные тесты

📊 Allure отчеты с графиками и статистикой

🎯 Pytest framework с маркерами и параметризацией

📝 Логирование всех запросов и ответов

🔧 Конфигурируемые настройки

🐳 Генерация тестовых данных через Pydantic модели

🛠 Предварительные требования
Python 3.8 или выше

pip (пакетный менеджер Python)

Git

Allure Framework (для генерации отчетов)

📦 Установка
Клонируйте репозиторий:

bash
git clone https://github.com/eabdikhalyk/booker_api.git
cd booker_api
Создайте виртуальное окружение:

bash
python -m venv .venv
Активируйте виртуальное окружение:

bash
# Для Windows:
.venv\Scripts\activate

# Для Linux/Mac:
source .venv/bin/activate
Установите зависимости:

bash
pip install -r requirements.txt
Установите Allure Framework:

bash
# Через scoop (Windows):
scoop install allure

# Через chocolatey (Windows):
choco install allure

# Через npm:
npm install -g allure-commandline

# Для других ОС смотрите: https://docs.qameta.io/allure/
🚀 Запуск тестов
Базовый запуск
bash
# Простой запуск всех тестов
pytest

# Запуск с подробным выводом
pytest -v

# Запуск с генерацией Allure результатов
pytest --alluredir=allure-results
Запуск конкретных тестов
bash
# Запуск только позитивных тестов
pytest tests/test_booker_api.py

# Запуск только негативных тестов  
pytest tests/test_booker_api_negative.py

# Запуск тестов по маркеру
pytest -m "smoke" --alluredir=allure-results

# Запуск тестов по имени
pytest -k "test_create" --alluredir=allure-results
Полный цикл тестирования
bash
# Очистка, запуск тестов и генерация отчета
pytest --alluredir=allure-results --clean-alluredir
allure generate allure-results -o report --clean
allure open report
📁 Структура проекта
text
booker_api/
├── config/                 # Конфигурационные файлы
│   ├── base_requests.py   # Базовые HTTP запросы
│   ├── setting.py         # Настройки и конфигурация
│   └── logger_config.py   # Конфигурация логгера
├── data/                  # Генераторы тестовых данных
│   └── generator.py       # Генерация тестовых данных
├── tests/                 # Тестовые сценарии
│   ├── conftest.py        # Pytest фикстуры
│   ├── test_booker_api.py # Позитивные тесты
│   └── test_booker_api_negative.py # Негативные тесты
├── logs/                  # Логи выполнения (авто)
├── allure-results/        # Результаты Allure (авто)
├── report/                # Готовые отчеты
├── requirements.txt       # Зависимости проекта
├── pytest.ini            # Конфигурация Pytest
└── README.md             # Документация
📊 Генерация отчетов
Создание Allure отчета
bash
# Генерация HTML отчета
allure generate allure-results -o report --clean

# Просмотр отчета в браузере
allure open report

# Или напрямую из результатов
allure serve allure-results
Одной командой (PowerShell)
powershell
pytest; allure generate allure-results -o report --clean; allure open report
Для CMD/Bash
bash
pytest && allure generate allure-results -o report --clean && allure open report
🏷 Маркеры тестов
Проект использует следующие маркеры:

@pytest.mark.order(n) - Определяет порядок выполнения тестов

@pytest.mark.negative - Негативные тест-кейсы

@pytest.mark.smoke - Smoke-тесты (основная функциональность)

@pytest.mark.regression - Регрессионные тесты

🧪 Примеры тестов
Позитивные тесты включают:
✅ Создание бронирования

✅ Получение бронирования по ID

✅ Полное обновление бронирования

✅ Частичное обновление бронирования

✅ Удаление бронирования

Негативные тесты включают:
❌ Неверные credentials аутентификации

❌ Невалидные данные бронирования

❌ Операции с несуществующим booking ID

❌ Неверные методы HTTP

⚠️ Устранение проблем
Ошибка: "No such file or directory: 'logs/api.log'"
bash
# Создайте папку logs
mkdir logs
Ошибка: "ModuleNotFoundError"
Убедитесь, что виртуальное окружение активировано и зависимости установлены:

bash
.venv\Scripts\activate
pip install -r requirements.txt
Предупреждения Pydantic
Замените в data/generator.py:

python
# Старая версия:
return data.dict()

# Новая версия:
return data.model_dump()
Предупреждения о неизвестных маркерах
Добавьте в pytest.ini:

ini
[pytest]
markers =
    order: порядок выполнения тестов
    negative: негативные тесты
    smoke: smoke тесты
    regression: regression тесты
📞 Поддержка
Если у вас возникли вопросы или проблемы:

Проверьте установлены ли все предварительные требования

Убедитесь что зависимости установлены: pip list

Проверьте что Allure установлен: allure --version

📄 Лицензия
Этот проект предназначен для образовательных целей и обучения автоматизации тестирования API.

Примечание: Все отчеты сохраняются в папке report/. Для просмотра откройте report/index.html в любом браузере.

Happy Testing! 🚀
