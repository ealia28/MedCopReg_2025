# Базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements.txt из подпапки clinic_app
COPY clinic_app/requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код приложения
COPY clinic_app/ .

# Открываем порт Flask (обычно 5000)
EXPOSE 5000

# Команда запуска Flask-приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
