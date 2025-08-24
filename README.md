# Booker API

**Booker API** — быстрый и удобный набор REST-эндпоинтов для управления бронированиями (CRUD), написанный на Python и покрытый API-тестами с помощью pytest и Allure.

## 🚀 Быстрый старт

1. **Клонируй репозиторий и перейди в папку проекта:**
   ```bash
   git clone https://github.com/eabdikhalyk/booker_api.git
   cd booker_api

2. **Создай виртуальное окружение и активируй его:**
   ```bash
   python -m venv .venv
   Активация для PowerShell / Windows:
   powershell
   .\.venv\Scripts\Activate

3. **Установи зависимости:**
   ```bash
   pip install -r requirements.txt

## 🧪 Запуск тестов
1. **По умолчанию тесты запускаются так:**

   ```bash
   pytest
   
   Результаты сохраняются в allure-results/ (см. pytest.ini).

2. **Для генерации и просмотра отчёта:**

   ```bash
   allure serve allure-results

3. **📝 Логирование**
Логи пишутся в файл logs/api.log.


## 📂 Структура проекта

```text
├── config/
│   ├── base_requests.py      — базовые HTTP-запросы и логгер
│   └── logger_config.py      — настройка логирования (создаёт папку log’ов)
├── data/                     — фикстуры или входные данные тестов
├── logs/                     — логи тестов и приложения
├── report/                   — Allure-отчёты
├── schemas/                  — схемы JSON-ответов (если используются)
├── tests/                    — тесты для API
├── pytest.ini                — конфигурация pytest (по умолчанию собирает Allure-результаты)
├── requirements.txt          — внешние зависимости (например, pytest, allure-pytest)
└── README.md                 — этот файл
