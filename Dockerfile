# Використовуємо офіційний Python-образ
FROM python:3.10

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо всі файли в контейнер
COPY . .

# Встановлюємо залежності (Flask)
RUN pip install --no-cache-dir flask

# Відкриваємо порт 3000
EXPOSE 3000

# Запускаємо додаток
CMD ["python", "app.py"]
