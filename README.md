
# Booker API

**Booker API** — быстрый и удобный набор REST-эндпоинтов для управления бронированиями (CRUD), написанный на Python и покрытый API-тестами с помощью pytest и Allure.

##  Особенности
- Создание, чтение, обновление и удаление ресурсов бронирования  
- Возможность запуска тестов с отчётностью Allure  
- Лёгкая настройка логирования с автоматическим созданием папки `logs/`

##  Содержание проекта
```text
├── config/
│   ├── base_requests.py      — базовые HTTP-запросы и логгер  
│   └── logger_config.py      — настройка логирования (создаёт папку log’ов)  
├── data/                      — фикстуры или входные данные тестов  
├── logs/                      — логи тестов и приложения  
├── report/                    — Allure-отчёты  
├── schemas/                   — схемы JSON-ответов (если используются)  
├── tests/                     — тесты для API  
├── pytest.ini                 — конфигурация pytest (по умолчанию собирает Allure-результаты)  
├── requirements.txt           — внешние зависимости (например, pytest, allure-pytest)  
└── README.md                  — этот файл
```text

##  Быстрый старт

**Клонируй репозиторий и перейди в папку проекта:**

git clone https://github.com/eabdikhalyk/booker_api.git
cd booker_api


**Создай виртуальное окружение и активируй его:**
```text
python -m venv .venv
.\.venv\Scripts\Activate  # для PowerShell / Windows


**Установи зависимости:**

pip install -r requirements.txt


**Убедись, что папка logs/ создана или дай приложению создать её (обычно логгер создаёт папку сам при выполнении).**

##  Запуск тестов 

По умолчанию тесты запускаются так:

pytest


— и результаты сохраняются в allure-results/ (см. pytest.ini).

**Для генерации и просмотра отчёта:**

allure serve allure-results

**Логирование**

Логи пишутся в файл logs/api.log. Если папки logs нет — она будет создана автоматически (logger_config.py). Это избавляет от ошибок вроде FileNotFoundError.

Пример использования
from config.base_requests import post_request, logger

logger.info("Создаём бронирование...")
response = post_request("/api/bookings", json={"name": "Alice", "date": "2025-09-01"})

Участие в разработке (Contributing)

Форкни проект

**Создай ветку:**

git checkout -b feature/new-endpoint


**Сделай изменения и протестируй локально (не забудь про Allure)**

**Сделай коммит и отправь в свой форк:**

git commit -m "Добавлен новый endpoint для ... "
git push origin feature/new-endpoint


**Открой Pull Request — я с удовольствием посмотрю!**

