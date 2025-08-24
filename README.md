# Booker API

**Booker API** — быстрый и удобный набор REST-эндпоинтов для управления бронированиями (CRUD), написанный на Python и покрытый API-тестами с помощью pytest и Allure.

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




🚀 Быстрый старт
1. Клонируй репозиторий и перейди в папку проекта:
bash
git clone https://github.com/eabdikhalyk/booker_api.git
cd booker_api
2. Создай виртуальное окружение и активируй его:
bash
python -m venv .venv
Активация для PowerShell / Windows:
powershell
.\.venv\Scripts\Activate
Активация для Linux/Mac:
bash
source .venv/bin/activate
3. Установи зависимости:
bash
pip install -r requirements.txt
4. Убедись, что папка logs/ создана или дай приложению создать её
Обычно логгер создаёт папку сам при выполнении. Если возникнет ошибка - создай вручную:

bash
mkdir logs
🧪 Запуск тестов
По умолчанию тесты запускаются так:

bash
pytest
Результаты сохраняются в allure-results/ (см. pytest.ini).

Для генерации и просмотра отчёта:

bash
allure serve allure-results
📝 Логирование
Логи пишутся в файл logs/api.log. Если папки logs нет — она будет создана автоматически (logger_config.py). Это избавляет от ошибок вроде FileNotFoundError.
